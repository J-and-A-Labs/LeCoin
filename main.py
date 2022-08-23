from Block import Block
from Pool import Pool
import random


pool = Pool()

block = Block("dn", "uhkuyibkj", pool)

print(pool.queue)

while not pool.queue[0].approved:
    mine = input("Would you like to start mining?")
    if mine == "y":
        pow = random.randint(1,1000)
        print(pow)
        pool.queue[0].calculateHash(pow) 
        print(pool.queue[0].hash)
    else:
        print("Mining Cancelled.")

print(f"Proof of work has been done for Block with Id {block.blockId} with challenge number {pow}.")

