import hashlib
import time

class Transaction:
    def __init__(self, from_addr, to_addr, amount):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.amount = amount

class Block:
    def __init__(self, timestamp, transactions, prior_hash=''):
        self.timestamp = timestamp  # Kiedy powstał blok
        self.transactions = transactions  # Transakcje w bloku
        self.prior_hash = prior_hash  # Hash poprzedniego bloku
        self.nonce = 0  # Inicjalizacja nonce na zero
        self.hash = self.create_hash()  # Stworzenie hash'a na podstawie zawartości bloku

    def create_hash(self):
        # Obliczenie hash'a bloku
        block_string = (str(self.prior_hash) + str(self.timestamp) +
                        str(self.transactions) + str(self.nonce)).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        # Kopanie bloku, aż hash zacznie się od trzech ostatnich cyfr numeru indeksu (456)
        while not self.hash.startswith('51897'):
            self.nonce += 1
            self.hash = self.create_hash()
        print(f"Blok wykopany! \nPoprzedni Hash: {self.prior_hash} \nNonce: {self.nonce} \nHash: {self.hash}")

class JanKowalskiBlock:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2  # Ustawienie poziomu trudności kopania
        self.pending_transactions = []  # Przechowywanie oczekujących transakcji
        self.mining_reward = 10  # Ustawienie nagrody za kopanie

    def create_genesis_block(self):
        # Genesis blok z numerem indeksu 123456 uzupełnionym zerami
        index_number = '279518'.zfill(64)
        genesis_transaction = Transaction('system', 'user', 0)
        return Block(time.time(), [genesis_transaction], "0")

    def get_last_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, mining_reward_address):
        # Stworzenie nowego bloku z wszystkimi oczekującymi transakcjami
        start_time = time.time()
        block = Block(time.time(), self.pending_transactions, self.get_last_block().hash)
        block.mine_block(self.difficulty)
        end_time = time.time()
        print(f"Czas potrzebny do wykopania bloku: {end_time - start_time} sekund")
        # Dodanie nowo wykopanego bloku do łańcucha
        self.chain.append(block)
        # Zresetowanie listy oczekujących transakcji i dodanie transakcji nagrody dla górnika
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

            # Sprawdzenie, czy hash obecnego bloku jest poprawny
            if current_block.hash != current_block.create_hash():
                return False

            # Sprawdzenie, czy obecny blok wskazuje na poprawny poprzedni blok
            if current_block.prior_hash != previous_block.hash:
                return False

        return True

# Stworzenie nowego łańcucha bloków
weronika_coin = JanKowalskiBlock()

# Stworzenie transakcji
weronika_coin.create_transaction(Transaction('address1', 'address2', 75))
weronika_coin.create_transaction(Transaction('address2', 'address3', 25))
weronika_coin.create_transaction(Transaction('address3', 'address4', 50))
weronika_coin.create_transaction(Transaction('address4', 'address5', 30))
weronika_coin.create_transaction(Transaction('address5', 'address1', 20))


weronika_coin.mine_pending_transactions('miner-address')
print(f"\nSaldo po 1 kopaniu: {weronika_coin.get_balance_of_address('miner-address')}")

weronika_coin.mine_pending_transactions('miner-address')
print(f"\nSaldo po 2 kopaniu: {weronika_coin.get_balance_of_address('miner-address')}")

weronika_coin.mine_pending_transactions('miner-address')
print(f"\nSaldo po 3 kopaniu: {weronika_coin.get_balance_of_address('miner-address')}")

weronika_coin.mine_pending_transactions('miner-address')
print(f"\nSaldo po 3 kopaniu: {weronika_coin.get_balance_of_address('miner-address')}")

weronika_coin.mine_pending_transactions('miner-address')
print(f"\nSaldo po 4 kopaniu: {weronika_coin.get_balance_of_address('miner-address')}")

