import uuid
from coin.chain import blockchain as bc
from coin.pending import pending

class Transaction:

    def __init__(self, sender, reciver, amount):

        self.id = uuid.uuid4()
        self.sender = sender
        self.reciver = reciver
        self.amount = amount
        self.transactions = {
            'self_sender': self.sender,
            'self_amount': str(self.amount),
            'self_reciver': self.reciver,
            'self_id': self.id
        }
    
    



        



