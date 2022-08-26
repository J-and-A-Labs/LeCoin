from block import Block
from pool import Pool
import random


pool = Pool()


transaction = Block.create_transaction(Block,"uwuad",pool)
transaction = Block.create_transaction(Block,"asdasd",pool)
transaction = Block.create_transaction(Block,"gdgdfg",pool)
transaction = Block.create_transaction(Block,"fdgdfhfhd",pool)
print(pool.queue)




mine = input("Would you like to  mine?")
if mine == "y":
    print(Block().check_aprove())
else:
    print("Mining Cancelled.")


print(
    f"Proof of work has been done for Block with:\nid: {block.blockId}\nhash: {hash}\nchallenge_number: {pow} ")
