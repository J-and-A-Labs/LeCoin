from coin.block import Block
from coin.transactions import Transaction
import hashlib
from time import time
import json
from coin.chain import blockchain as bc
from coin.pending import pending





class BlockChain:

    def __init__(self):
        self.chain = bc
        self.difficulty = 4
        self.mine_reward = 69
        self.pending_transactions = pending
        self.chain.append(self.genesis_block())

    def genesis_block(self):
        block = Block(len(bc),time(), [], "0")
        chain = {
                "index": block.index,
                "timestamp": block.timestamp,
                "transactions": block.transactions,
                "previous_hash": block.prev_hash,
                "block_hash": block.block_hash,
        }
        return chain

    def get_recent_block(self):
        if (self.chain[len(self.chain) - 1]) is None:
            return [(self.chain[len(self.chain) - 1])]
        else:
            chain =  (self.chain[len(self.chain) - 1])
            return chain["block_hash"]


    def mine(self):
        block = Block(len(bc),time(), self.pending_transactions, self.get_recent_block())
        block_hash = block.mine(self.difficulty)
        print(f"Coin has been mined.\nHash:{block_hash}\n")
        print(block_hash)
        chain = {
                "index": block.index,
                "timestamp": block.timestamp,
                "transactions": block.transactions,
                "previous_hash": block.prev_hash,
                "block_hash": block.block_hash,
        }
        self.chain.append(chain)
        self.pending_transactions = []

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)
        print("Transaction has been added to the queue.")

    def get_block_chain(self):
        print(self.chain)

    def get_pending_transactions(self):
        print(self.pending_transactions)



