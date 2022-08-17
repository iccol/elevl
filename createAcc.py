import requests

from stellar_sdk import Keypair

keypair = Keypair.random()

print("Public key: "+keypair.public_key)
print("Secret seed: "+keypair.secret)

url = "https://friendbot.stellar.org"

response = requests.get(url, params={"addr": keypair.public_key})
print(response)