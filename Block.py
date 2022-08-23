import hashlib


class Block:

  

    #Add Transaction class Here
   def __init__(self,prevHash,blockId,pool):
        self.approved = False
        self.prevHash = prevHash
        self.blockId = blockId
        self.pool = pool
        self.calculateIncompleteHash("ygjkgjhh")
        pool.append(self)




   def calculateIncompleteHash(self,transactionHash):
        encodedIncompleteHash = (transactionHash+self.prevHash+self.blockId).encode()
        incompleteHash = hashlib.sha256(encodedIncompleteHash).hexdigest() 

        int_value = int(incompleteHash, base=16)

        self.incompleteHash = str(bin(int_value))




        #Blocks being push on to pool goes here


   def calculateHash(self, ProofOfWork):
         encodedHash = (self.incompleteHash + str(ProofOfWork)).encode()
         hash = hashlib.sha256(encodedHash).hexdigest()

         int_value = int(hash, base=16)

         self.hash = str(bin(int_value))[2:]


         if self.hash[0] == "1":
          if self.hash[1] == "1":   
               self.approved = True
         
      
      #Add block broadcasting and chianing here
   
   




         

        





