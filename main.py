from blockchain import BlockChain
from transactions import Transaction



LeCoin = BlockChain()

# create one transaction worth 50 LeCoins(function should also include wallet address)
print("\nCreating transaction worth 50 LeCoins.")
transaction_1 = Transaction("bobvWallet", "apeWallet", 50)
LeCoin.create_transaction(transaction_1.transaction_string)

# create another transaction worth 250 LeCoins(function should also include wallet address)
print("\nCreating transaction worth 250 LeCoins.")
transaction_2 = Transaction("apeWallet", "bobWallet", 250)
LeCoin.create_transaction(transaction_2.transaction_string)

# print the pending transactions
print("\nHere are the pending_transactions.")
LeCoin.get_pending_transactions()

# mine the coin
print("\nCoin is being mined...")
LeCoin.mine()

# print the blockchain
print("Here is the blockchain.")
LeCoin.get_block_chain()