from stellar_sdk import Server,TransactionBuilder,Keypair,Network
import time

start_time = time.time()

server = Server(horizon_url="https://horizon-testnet.stellar.org")

acc1_keypair = Keypair.from_secret("SDBERY63TAQA4SMFNCZUAB5OVHXWQC477RA2WPO2YW77BRUR5CJQLVGA")
acc1 = server.load_account(account_id=acc1_keypair.public_key)

temp = Keypair.random() # Temporary multi party account
amount = 100    # Negotiated default amount

print(" Temp Details generated")
print("Public key: "+temp.public_key)
print("Secret seed: "+temp.secret)

# Creating temporary account
transaction1 = TransactionBuilder(
    source_account=acc1,
    network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
    base_fee=100).append_create_account_op(
        destination=temp.public_key,
        starting_balance=str(amount+1)
    ).build()

transaction1.sign(acc1_keypair)
response1 = server.submit_transaction(transaction1)
print("Transaction hash: {}"+format(response1["hash"]))
print("---%s seconds --" % (time.time() - start_time))
