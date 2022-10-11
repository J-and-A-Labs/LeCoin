from coin.blockchain import BlockChain
from coin.transactions import Transaction



LeCoin = BlockChain()

# create one transaction worth 50 LeCoins(function should also include wallet address)
print("\nCreating transaction worth 50 LeCoins.")
transaction_1 = Transaction("bobvWallet", "apeWallet", 50)
LeCoin.create_transaction(transaction_1.transactions)

# create another transaction worth 250 LeCoins(function should also include wallet address)
print("\nCreating transaction worth 250 LeCoins.")
transaction_2 = Transaction("apeWallet", "bobWallet", 250)
LeCoin.create_transaction(transaction_2.transactions)

# print the pending transactions
print("\nHere are the pending_transactions.")
LeCoin.get_pending_transactions()

# mine the coin
print("\nCoin is being mined...")
LeCoin.mine()

#reward miner for transaction(IMPLEMENT SENDER AND RECEPIENT)
reward_1 = Transaction("bobWallet", "apeWallet", 69)
LeCoin.create_transaction(reward_1.transactions)
print(f"\nMiner has been awarded 69 coins.")
LeCoin.get_pending_transactions()

# print the blockchain
print("\nHere is the blockchain.")
LeCoin.get_block_chain()


