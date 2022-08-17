from stellar_sdk import Server,TransactionBuilder,Signer,Network,Keypair
import time

start_time = time.time()

server = Server(horizon_url="https://horizon-testnet.stellar.org")

# Escrow account secret key
acc1_keypair = Keypair.from_secret("SDXUXB54DPAYGA45ZTDXFB3LGHFYMQQ5WQLK6P3CW6HZAFTI67DC6COE")
acc1 = server.load_account(account_id=acc1_keypair.public_key)



# Adding secondary signer to temporary account
acc2_keypair = Keypair.from_public_key("GDHC2BG7GJ5RI3IF64E27CB3DRTCKM65XLYEU4S7VNK3NU77JVCKGVHP")
acc2_signer = Signer.ed25519_public_key(account_id=acc2_keypair.public_key, weight=1)
transaction = TransactionBuilder(
    source_account=acc1,
    network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
    base_fee=100).append_set_options_op(
        master_weight=1,
        low_threshold=1,
        med_threshold=2,
        high_threshold=2,
        signer=acc2_signer).set_timeout(30).build()

#Signing the transaction after Charging is over
transaction.sign(acc1_keypair)
response = server.submit_transaction(transaction)
print(response)
print("---%s seconds --" % (time.time() - start_time))      
