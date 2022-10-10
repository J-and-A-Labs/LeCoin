import hashlib


class Block:

    def __init__(self,index, timestamp, transactions, prev_hash = "0"):
        self.index = index
        self.prev_hash = prev_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.block_hash = 0 #updated by the create_hash() function
        self.block_mine_hash = 0 #updated by the create_hash() function
        self.block = 0 
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
        self.block = block
        return block

    def mine(self, mining_dificulty):
        while self.approved is False:
            self.pow += 1
            self.hash = self.create_hash()
            print(f"Guess_{self.pow}:{self.block_mine_hash}\n")
            if self.block_mine_hash[:mining_dificulty] == "1111":  #note, when changing the difficulty, you might need to add or remove a 1
                self.approved = True
                return self.block_mine_hash

    
    