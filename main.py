from coin.blockchain import BlockChain
from coin.transactions import Transaction
import rsa
import os

LeCoin = BlockChain()



if os.path.exists("publicKey.pem") ==0:
    
    publicKey, privateKey = rsa.newkeys(1024)

    with open("publicKey.pem", "wb") as f:
        f.write(publicKey.save_pkcs1("PEM"))

    with open("privateKey.pem", "wb") as f:
        f.write(privateKey.save_pkcs1("PEM"))





with open("publicKey.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())



def makeTransaction():
    reciver  = input("Enter Reciver: ")
    amount = input("Enter Amount: ")

    transaction = Transaction(reciver, amount)
    LeCoin.create_transaction(transaction.transactions, transaction.signature)

def mine():
    LeCoin.mine()
    #TODO Add a Reward Here. 




while 1:

    print(f"Hello (Persons Name).")
    choice = input("To Send Lecoin: 1 \n To Mine : 2 \n To see Blockchain: 3 \n To see pending transactions: 4\n" )

    if choice == "1":
        os.system("cls")
        makeTransaction()

        #Adding temporary transaction because block can be mined with 2 transactions

        makeTransaction()


    if choice == "2":
        os.system("cls")
        mine()

    if choice == "3":
        os.system("cls")
        print(LeCoin.get_block_chain())
    if choice =="4":
        os.system("cls")
        print(LeCoin.get_pending_transactions())























'''
reward_1 = Transaction("bobWallet", "apeWallet", 69)
LeCoin.create_transaction(reward_1.transactions)
print(f"\nMiner has been awarded 69 coins.")
LeCoin.get_pending_transactions()
'''




