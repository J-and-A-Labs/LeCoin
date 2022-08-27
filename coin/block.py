import hashlib


class Block:

    def __init__(self, timestamp, transactions, prev_hash = "0"):
        self.prev_hash = prev_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.pow = 0
        self.hash = self.create_hash()
        self.approved = False

    def create_hash(self):
        encodedIncompleteHash = (str(self.prev_hash) + str(self.pow) + str(self.timestamp) + str(self.transactions)).encode()
        incompleteHash = hashlib.sha256(encodedIncompleteHash).hexdigest()
        int_value = int(incompleteHash, base=16)
        hash = str(bin(int_value))[2:]
        return hash

    def mine(self, mining_dificulty):
        while self.approved is False:
            self.pow += 1
            self.hash = self.create_hash()
            print(f"Guess_{self.pow}:{self.hash}\n")
            if self.hash[:mining_dificulty] == "1111":  #note, when changing the difficulty, you might need to add or remove a 1
                self.approved = True
                return self.hash