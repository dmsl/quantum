import random


class RandomBinary:

    @classmethod
    def generate_random_binary(cls, limit: int) -> str:
        rand = int(random.uniform(0, limit))
        print(f"random binary in decimal:{rand}")
        random_bin = bin(rand)[2:]
        print(random_bin)
        return random_bin

    @classmethod
    def generate_random_binary_v2(cls, binary_length: int) -> str:
        random_bin = ""
        for i in range(binary_length):
            rand = int(random.uniform(0, 1))
            if rand >= 0.5:
                random_bin = random_bin + "1"
            else:
                random_bin = random_bin + "0"
        return random_bin
