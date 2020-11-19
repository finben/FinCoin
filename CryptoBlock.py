from hashlib import sha256


class Block:
    def __init__(self, index, transactions, timestamp):
        """
        Constructor for the block class 
        :param index: Unique id for the block
        :param transaction: List of transactions
        :param timestamp: Time of generation of the block
        """

        self.index = index
        self.tranactions = transactions
        self.timestamp = timestamp

    def compute_hash(block):
        """ 
        Returns the hash of the block instance by first converting it to JSON then hashing
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()
