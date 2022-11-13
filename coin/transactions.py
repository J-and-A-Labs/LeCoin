import uuid
import rsa
import os








class Transaction:

    def __init__(self, reciver, amount):
        
        with open("publicKey.pem", "rb") as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())


        self.id = uuid.uuid4()
        self.sender = public_key
        self.reciver = reciver
        self.amount = amount
        self.transactions = {
            'sender': self.sender,
            'amount': str(self.amount),
            'reciver': self.reciver,
            'id': self.id,
        }
        self.sign(str(self.transactions))




    def sign(self,message):
        with open("privateKey.pem", "rb") as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read())
        self.signature = rsa.sign(message.encode(), private_key, "SHA-256" )


    



    
    









