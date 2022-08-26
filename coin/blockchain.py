import hashlib
from time import time
import json


class Block:

    def __init__(self, timestamp, transactions, prev_hash="0"):
        self.prev_hash = prev_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.pow = 0
        self.hash = self.create_hash()
        self.aproved = False

    def create_hash(self):
        encodedIncompleteHash = (
            str(self.prev_hash) + str(self.pow) + str(self.timestamp) + str(self.transactions)).encode()
        incompleteHash = hashlib.sha256(encodedIncompleteHash).hexdigest()
        int_value = int(incompleteHash, base=16)
        hash = str(bin(int_value))[2:]
        return hash

    def mine(self, mining_dificulty):
        while self.aproved is False:
            self.pow += 1
            self.hash = self.create_hash()
            print(f"Guess_{self.pow}:{self.hash}\n")
            if self.hash[:mining_dificulty] == "1111":  #note, when changing the difficulty, you might need to add or remove a 1
                self.approved = True
                return self.hash


class BlockChain:

    def __init__(self):
        self.chain = [self.genesis_block()]
        self.difficulty = 4
        self.mine_reward = 69
        self.pending_transactions = []

    def genesis_block(self):
        block = Block(time(), [], "0")
        block_hash = block.create_hash()
        return block_hash

    def get_recent_block(self):
        return self.chain[len(self.chain) - 1]

    def mine(self):
        block = Block(time(), self.pending_transactions, self.get_recent_block)
        block_hash = block.mine(self.difficulty)
        print(f"Coin has been mined.\nHash:{block_hash}\n")
        self.chain.append(block_hash)
        self.pending_transactions = []

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)
        print("Transaction has been added to the queue.")

    def get_block_chain(self):
        print(self.chain)

    def get_pending_transactions(self):
        print(self.pending_transactions)


# init the coin
LeCoin = BlockChain()

# create one transaction worth 50 LeCoins(function should also include wallet address)
print("\nCreating transaction worth 50 LeCoins.")
transaction_1 = 50
LeCoin.create_transaction(transaction_1)

# create another transaction worth 250 LeCoins(function should also include wallet address)
print("\nCreating transaction worth 250 LeCoins.")
transaction_2 = 250
LeCoin.create_transaction(transaction_2)

# print the pending transactions
print("\nHere are the pending_transactions.")
LeCoin.get_pending_transactions()

# mine the coin
print("\nCoin is being mined...")
LeCoin.mine()

# print the blockchain
print("Here is the blockchain.")
LeCoin.get_block_chain()
