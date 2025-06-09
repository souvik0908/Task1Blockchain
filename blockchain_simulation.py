import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_data = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_data.encode()).hexdigest()

genesis = Block(0, "Genesis Block", "0")
block1 = Block(1, "Block 1 Data", genesis.hash)
block2 = Block(2, "Block 2 Data", block1.hash)

blockchain = [genesis, block1, block2]

for block in blockchain:
    print(f"Block {block.index}:\nHash: {block.hash}\nPrevious Hash: {block.previous_hash}\n")


block1.data = "Tampered Data"
block1.hash = block1.compute_hash()
print("After Tampering Block 1:")
for block in blockchain:
    print(f"Block {block.index}:\nHash: {block.hash}\nPrevious Hash: {block.previous_hash}\n")
