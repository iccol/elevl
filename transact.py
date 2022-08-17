from stellar_sdk import Server,TransactionBuilder,Signer,Network,Keypair,TransactionEnvelope
import time

start_time = time.time()

server = Server(horizon_url="https://horizon-testnet.stellar.org")

# Escrow account
acc1_keypair = Keypair.from_secret("SDXUXB54DPAYGA45ZTDXFB3LGHFYMQQ5WQLK6P3CW6HZAFTI67DC6COE")
acc1 = server.load_account(account_id=acc1_keypair.public_key)
amount = 10  # After charging
# Vehicle prepares the transaction
dest_id = "GDHC2BG7GJ5RI3IF64E27CB3DRTCKM65XLYEU4S7VNK3NU77JVCKGVHP"

transaction = TransactionBuilder(
    source_account=acc1,
    network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
    base_fee=100).append_payment_op(
        destination=dest_id,
        amount = str(amount),
        asset_code="XLM").set_timeout(30).build()

#Signing the transaction after charging is done
transaction.sign(acc1_keypair)

# send this to Secondary account to sign
send = transaction.to_xdr()

print("---%s seconds --" % (time.time() - start_time))  
print(send)

# CP Receives signed token from User
transaction2 = TransactionEnvelope.from_xdr(send,Network.TESTNET_NETWORK_PASSPHRASE)
sign2 = "SCJ645MGVQ7O2DYQGRYQS7J7LNULJCYYPF6KEQICESBDWRU2PIRCKPVU"
transaction2.sign(sign2)

# Submits the transaction after signing
response = server.submit_transaction(transaction2)
print(response)
print("---%s seconds --" % (time.time() - start_time))  
# resp = transaction.sign(acc1_keypair)
# transaction.sign(acc1_keypair)
# response = server.submit_transaction(transaction)
# print(response)
