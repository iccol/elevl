from stellar_sdk import Server

server = Server(horizon_url="https://horizon-testnet.stellar.org")

transactions = server.transactions().for_account(account_id="GC7HTQEBNJK7IPTG4YLT7VWGWXJ5RA7VGSVOJ5XV6LTYDMO4QZ2ZSQGF").call()

print(transactions)