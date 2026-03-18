import hashlib
import time

class Transaction:
    def __init__(self, from_addr, to_addr, amount):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.amount = amount

class Block:
    def __init__(self, timestamp, transactions, prior_hash=''):
        self.timestamp = timestamp  # When the block was created
        self.transactions = transactions  # The transactions within this block
        self.prior_hash = prior_hash  # The hash of the previous block
        self.nonce = 0  # Initialize nonce to zero
        self.hash = self.create_hash()  # Create the hash based on the block's contents

    def create_hash(self):
        # Calculate the hash for the block
        block_string = (str(self.prior_hash) + str(self.timestamp) +
                        str(self.transactions) + str(self.nonce)).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        # Mine the block until the hash starts with a number of zeros equal to difficulty
        #target = '0' * difficulty
        while not self.hash.endswith('518'):
            self.nonce += 1
            self.hash = self.create_hash()
        print(f"Block mined! Nonce: {self.nonce}, Hash: {self.hash}")

class WeronikaWalczukBlock:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2  # Set mining difficulty
        self.pending_transactions = []  # Store transactions that are yet to be mined
        self.mining_reward = 10  # Set mining reward

    def create_genesis_block(self):
        return Block(time.time(), [], "0")

    def get_last_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, mining_reward_address):
        # Create a new block with all pending transactions
        block = Block(time.time(), self.pending_transactions, self.get_last_block().hash)
        block.mine_block(self.difficulty)

        # Add the newly mined block to the chain
        self.chain.append(block)

        # Reset the list of pending transactions and add a transaction to reward the miner
        self.pending_transactions = [Transaction(None, mining_reward_address, self.mining_reward)]

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def get_balance_of_address(self, address):
        balance = 0

        for block in self.chain:
            for transaction in block.transactions:
                if transaction.from_addr == address:
                    balance -= transaction.amount
                if transaction.to_addr == address:
                    balance += transaction.amount

        return balance

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the hash of the current block is correct
            if current_block.hash != current_block.create_hash():
                return False

            # Check if the current block points to the correct previous block
            if current_block.prior_hash != previous_block.hash:
                return False

        return True

# Create a new instance of the Blockchain
ernesto_coin = WeronikaWalczukBlock()

# Create some transactions
ernesto_coin.create_transaction(Transaction('address1', 'address2', 75))
ernesto_coin.create_transaction(Transaction('address2', 'address1', 25))

# Mine the pending transactions
print("Starting mining process...")
ernesto_coin.mine_pending_transactions('miner-address')

# Check the balance of the miner
print(f"\nBalance: {ernesto_coin.get_balance_of_address('miner-address')}")

# Mine again to receive the reward
print("Mining again to receive the reward...")
ernesto_coin.mine_pending_transactions('miner-address')

# Check the balance of the miner again
print(f"\nBalance after second mining: {ernesto_coin.get_balance_of_address('miner-address')}")