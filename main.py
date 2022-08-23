from Block import Block
from Pool import Pool
import random


pool = Pool()

block = Block("dn", "uhkuyibkj", pool)

print(pool.queue)
mine = input("Would you like to  mine?")
if mine == "y":
    while not pool.queue[0].approved:
        pow = random.randint(1,1000)
        print(pow)
        calculate_hash = pool.queue[0].calculateHash(pow) 
        print(pool.queue[0].hash)
        hash = calculate_hash
else:
    print("Mining Cancelled.")

    

print(f"Proof of work has been done for Block with:\nid: {block.blockId}\nhash: {hash}\nchallenge_number: {pow} ")

