import uuid
from coin.chain import blockchain as bc
from coin.pending import pending

class Transaction:

    def __init__(self, sender, reciver, amount):

        self.id = uuid.uuid4()
        self.sender = sender
        self.reciver = reciver
        self.amount = amount
        self.transaction_string = self.sender + str(self.amount) + self.reciver + str(self.id)
    
    



        



