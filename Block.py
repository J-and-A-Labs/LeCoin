import hashlib
from time import time
from pool import Pool
from turtle import Pen


pool = Pool()
class Block:

    # Add Transaction class Here
     def __init__(self):
          self.approved = False
          self.block_chain = []
          self.create_block(prev_hash = 0, proof=0, pool = pool)

     def create_block(self,prev_hash,proof,pool):
          index = len(self.block_chain) + 1 #current index in chain + 1
          timestamp = time()
          pending_transactions_obj = pool.show()
          if pending_transactions_obj is None:
               pending_transactions_obj = []
          pending_transactions = []
          for obj in pending_transactions_obj:
               pending_transactions.append(obj)
          prev_hash = prev_hash
          proof = proof
          block = {
               "index": index,
               "timestamp": timestamp,
               "pending_transactions": pending_transactions,
               "previous_hash": prev_hash,
               "proof_of_work": proof
          }
          pool = pool.clear()
          self.block_chain.append(block)
          return block


     def create_transaction(self,transaction_data,pool):
          pool.append(transaction_data)

          return "transaction added to pool."



     def calculateIncompleteHash(self, transactionHash):
          encodedIncompleteHash = (transactionHash+self.prevHash+self.blockId).encode()
          incompleteHash = hashlib.sha256(encodedIncompleteHash).hexdigest()

          int_value = int(incompleteHash, base=16)

          self.incompleteHash = str(bin(int_value))

          # Blocks being push on to pool goes here

     def calculateHash(self, ProofOfWork):
          encodedHash = (self.incompleteHash + str(ProofOfWork)).encode()
          hash = hashlib.sha256(encodedHash).hexdigest()
          int_value = int(hash, base=16)
          self.hash = str(bin(int_value))[2:]
          if self.hash[:4] == "1111":
               self.approved = True
               return self.hash

          # Add block broadcasting and chianing here

     def calculateIncompleteHash_2(self,block):
          hash = block.encode()
          hash = hashlib.sha256(hash).hexdigest()
          int_value = int(hash, base=16)
          self.hash = str(bin(int_value))
     
     def check_aprove(self):
          return self.approved