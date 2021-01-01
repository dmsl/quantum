class BitCombinations:

    @classmethod
    def split(cls, word: str) -> list:
        return [char for char in word]

    @classmethod
    def get_child(cls, parent: list) -> list:
        return parent.pop()

    @classmethod
    def count_ones(cls, binary_list: list) -> int:
        count = 0
        for bit in binary_list:
            if bit == "1":
                count = count + 1
        return count

    @classmethod
    def combinations(cls, bits: int) -> list:
        final_layer = []
        for n_bits in range(1, bits):
            parent = []
            for layer in range(bits - 1):
                new_layer = []
                if layer == 0:
                    parent = []
                    b0 = ["0"]
                    b1 = ["1"]
                    parent.append(b0)
                    parent.append(b1)
                while len(parent) > 0:
                    child = cls.get_child(parent)
                    new_child1 = ["1"]
                    new_child0 = ["0"]
                    remaining_ones_for_child = n_bits - cls.count_ones(child)
                    remaining_length = bits - len(child)
                    if remaining_ones_for_child == remaining_length:
                        new_child1.extend(child)
                        new_layer.append(new_child1)
                    elif 0 < remaining_ones_for_child < remaining_length:
                        new_child1.extend(child)
                        new_layer.append(new_child1)
                        new_child0.extend(child)
                        new_layer.append(new_child0)
                    elif remaining_ones_for_child == 0:
                        new_child0.extend(child)
                        new_layer.append(new_child0)
                parent = new_layer
            final_layer.append(parent)
        result = []
        all_zeros = [[cls.split("0" * bits)]]
        all_ones = [[cls.split("1" * bits)]]
        result.extend(all_zeros)
        result.extend(final_layer)
        result.extend(all_ones)
        return result

    @classmethod
    def produce_worse_scenario(cls, combos: list) -> list:
        worse_input_list = []
        even = []
        odd = []
        for i in range(len(combos)):
            if i % 2 == 1:  # list with even amount of zeroes and ones
                even.extend(combos[i])
            else:
                odd.extend(combos[i])
        worse_input_list.extend(even)
        worse_input_list.extend(odd)
        return worse_input_list
