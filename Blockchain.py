import CryptoBlock


class Blockchain:

    def __init__(self):
        self.chain = [CryptoBlock(0, [], time.time(), "0"]  # Genesis block creation

    @ property
    def last_block(self):
        return self.chain[-1]
