import hashlib
from time import time
class Block:

    def __init__(self,index, timestamp, transactions, prev_hash = "0"):
        self.index = index
        self.prev_hash = prev_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.block_hash = 0 #updated by the create_hash() function
        self.block_mine_hash = 0 #updated by the create_hash() function
        self.pow = 0
        self.hash = self.create_hash()
        
        self.approved = False

    def create_hash(self):

        # hash the block, preserving subcategories
        encodedIncompleteHash = (str(self.prev_hash) + str(self.pow) + str(self.timestamp) + str(self.transactions)).encode()
        block = hashlib.sha256(encodedIncompleteHash)

        # get the block hash
        block_hash = block.hexdigest()

        # get the block int hash(used for mining)
        int_value = int(block_hash, base=16)
        block_mine_hash = str(bin(int_value))[2:]

        self.block_mine_hash = block_mine_hash
        self.block_hash = block_hash
        return block



transactions = {"joe",15,"bob"}
block = Block(0,time(),transactions,0)
chain = {
    "chain":{
        "index": block.index,
        "timestamp": block.timestamp,
        "transactions": block.transactions,
        "previous_hash": block.prev_hash,
        "block_hash": block.block_hash,
        "block_mine_hash": block.block_mine_hash
    }
}
print(str(chain))