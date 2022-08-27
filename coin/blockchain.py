from block import Block
from transactions import Transaction
import hashlib
from time import time
import json
from chain import blockchain as bc
from pending import pending





class BlockChain:

    def __init__(self):
        self.chain = bc
        self.difficulty = 4
        self.mine_reward = 69
        self.pending_transactions = pending
        self.chain.append([self.genesis_block(),0])

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
        print(block_hash)
        self.chain.append(block_hash)
        self.pending_transactions = []

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)
        print("Transaction has been added to the queue.")

    def get_block_chain(self):
        print(self.chain)

    def get_pending_transactions(self):
        print(self.pending_transactions)



