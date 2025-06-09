import hashlib, time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        return hashlib.sha256(f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}".encode()).hexdigest()

    def mine_block(self, difficulty):
        prefix = '0' * difficulty
        attempts = 0
        start = time.time()
        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.compute_hash()
            attempts += 1
        end = time.time()
        print(f"Block mined: {self.hash}")
        print(f"Attempts: {attempts}, Time: {end - start:.2f} seconds")

block = Block(0, "Mining Block", "0")
block.mine_block(difficulty=4)
