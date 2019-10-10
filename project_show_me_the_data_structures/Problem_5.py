# Problem 5 - Blockchain

import sys
sys.path.append("c:/Users/M/Anaconda3/Lib/site-packages/")

# Your work here

import hashlib
import datetime

class Node:

    def __init__(self, block, previous=None):
        self.block = block
        self.previous = None

class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_block(self, data):

        previous_hash = None

        if self.tail:
            previous_hash = self.tail.block.hash

        block = Block(data, previous_hash)

        node = Node(block, self.tail)
        if self.head == None:
            self.head = node

        else:
            block.previous = self.tail
            block.previous_hash = self.tail.block.hash

        self.tail = node


class Block:

    def __init__(self, data, previous_hash=None, timestamp=datetime.datetime.utcnow()):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.data)

    def calc_hash(self, data):
        sha = hashlib.sha256()

        hash_str = "We are going to encode this string of data!".encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


print("Begin Blockchain testing...\n")
chain = Blockchain()
chain.add_block("test data")

print("chain.tail - ", chain.tail)
print("chain.head - ", chain.head)
print("\nPrint true or false for chain.tail == chain.head")
print(chain.tail == chain.head)

print("\nchain.tail.block.previous_hash - ", chain.tail.block.previous_hash)
print("\nPrint true or false for chain.tail.block.previous_hash == None")
print(chain.tail.block.previous_hash == None)

first_block_hash = chain.tail.block.hash

chain.add_block("more data")
print("\nchain.tail - ", chain.tail)
print("chain.head - ", chain.head)
print("\nPrint true or false for chain.tail != chain.head")
print(chain.tail != chain.head)

print("\nchain.tail.block.previous_hash - ", chain.tail.block.previous_hash)
print("\nPrint true or false for chain.tail.block.previous_hash != None")
print(chain.tail.block.previous_hash != None)

second_block_hash = chain.tail.block.hash
second_block_prev_hash = chain.tail.block.previous_hash

print("\nfirst_block_hash       - ", first_block_hash)
print("second_block_prev_hash - ", second_block_prev_hash)
print("\nPrint true or false for first_block_hash == second_block_prev_hash")
print(first_block_hash == second_block_prev_hash)

print("\nsecond_block_hash      - ", second_block_hash)
print("second_block_prev_hash - ", second_block_prev_hash)
print("\nPrint true or false for second_block_hash != second_block_prev_hash")
print(second_block_hash != second_block_prev_hash)

print('\nTest completed...')

# the above test cases should print the following:
"""
Begin Blockchain testing...

chain.tail -  <__main__.Node object at 0x0000027769B5D940>
chain.head -  <__main__.Node object at 0x0000027769B5D940>

Print true or false for chain.tail == chain.head
True

chain.tail.block.previous_hash -  None

Print true or false for chain.tail.block.previous_hash == None
True

chain.tail -  <__main__.Node object at 0x0000027769B5D9B0>
chain.head -  <__main__.Node object at 0x0000027769B5D940>

Print true or false for chain.tail != chain.head
True

chain.tail.block.previous_hash -  a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10

Print true or false for chain.tail.block.previous_hash != None
True

first_block_hash       -  a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
second_block_prev_hash -  a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10

Print true or false for first_block_hash == second_block_prev_hash
True

second_block_hash      -  a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
second_block_prev_hash -  a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10

Print true or false for second_block_hash != second_block_prev_hash
False

Test completed...


"""