import CryptoBlock


class Blockchain:

    def __init__(self):
        self.chain = [CryptoBlock(0, [], time.time(), "0"]  # Genesis block creation
        self.difficulty=2

    def proof_of_work(self, block):
        block.nonce=0
        computed_hash=block.compute_hash()

        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash=block.compute_hash()
        return computed_hash

    def add_block(self, block, proof):
        previous_hash=self.last_block.hash

        if previous_hash != block.previous_hash:
            return false

        if not Blockchain.is_valid_proof(block, proof):
            return false

        block.hash=proof
        self.chain.append(block)
        return True

    @ property
    def last_block(self):
        return self.chain[-1]
