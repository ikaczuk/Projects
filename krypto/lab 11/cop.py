import hashlib
import json
import time

class Transaction:
    def __init__(self, from_add, to_add, amount):
        self.from_add = from_add
        self.to_add = to_add
        self.amount = amount

class Block:
    def __init__(self, index, timestamp, data, prior_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prior_hash = prior_hash
        self.nonce = 0
        self.hash = self.create_hash()

    def create_hash(self):
        hashing = hashlib.sha256(f"{self.index}{self.prior_hash}{self.timestamp}{self.data}{self.nonce}".encode()).hexdigest()
        return hashing

    def mine_block(self, difficulty):
        # Loop until the hash begins with the required three digits (456)
        while not self.hash.endswith('518'):
            self.nonce += 1
            self.hash = self.create_hash()
            print('Block Hash: ' + self.hash)  # Optional: Print each hash attempt

class WeronikaWalczukBlockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # Set difficulty level

    def create_genesis_block(self):
        # Genesis block with index number
        index_number = '279518'.zfill(64)
        return Block(0, '04/17/1973', index_number, '0')

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.prior_hash = self.get_last_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_bc_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.create_hash():
                return False
            if current_block.prior_hash != previous_block.hash:
                return False
        return True

wer_coin = WeronikaWalczukBlockchain()
# Add three blocks to the blockchain
wer_coin.add_block(Block(1, '04/03/1977', 'amount = 7'))
wer_coin.add_block(Block(2, '04/05/1977', 'amount = 17'))
wer_coin.add_block(Block(3, '04/24/1977', 'amount = 77'))
# Print the blockchain to the console
print(json.dumps(wer_coin.chain, default=lambda o: o.__dict__, indent=4))
