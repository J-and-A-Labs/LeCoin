from Block import Block
from Pool import Pool
import random


pool = Pool()

block = Block("0000", "1", pool)

print(pool.queue)


while not pool.queue[0].approved:
    pow = random.randint(1,1000)
    print(pow)
    pool.queue[0].calculateHash(pow)
    print(pool.queue[0].hash)


print(f"Proof of work has been done for Block with Id {block.blockId} with challenge number {pow}")

