
import hashlib, time

class Block:
    def _init_(self, index, data, previous_hash, difficulty=3):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(content.encode()).hexdigest()

class Blockchain:
    def _init_(self, difficulty=3):
        self.difficulty = difficulty
        self.chain = []
        self.setBlock("Genesis Block")  

    def setBlock(self, data):
        prev_hash = self.chain[-1].hash if self.chain else "0"
        new_block = Block(len(self.chain), data, prev_hash, self.difficulty)
        mined = self.mineBlock(new_block)         # تعدين
        self.chain.append(mined)


    def getBlock(self, index):
        if 0 <= index < len(self.chain):
            b = self.chain[index]
            return {
                "index": b.index, "timestamp": b.timestamp, "data": b.data,
                "previous_hash": b.previous_hash, "nonce": b.nonce,
                "hash": b.hash
            }
        return None


    def blocksExplorer(self):
        return [self.getBlock(i) for i in range(len(self.chain))]


    def mineBlock(self, block):
        target_prefix = "0" * block.difficulty
        while True:
            block.hash = block.calculate_hash()
            if block.hash.startswith(target_prefix):

                return block
            block.nonce += 1

if _name_ == "_main_":
    bc = Blockchain(difficulty=4)  
    
    bc.setBlock("Tx 1: A -> B : 5")
    bc.setBlock("Tx 2: B -> C : 2")
    print("Block[1]:", bc.getBlock(1))
    print("Explorer:", bc.blocksExplorer())