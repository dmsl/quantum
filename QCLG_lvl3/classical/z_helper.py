# Obsolete
class Helper:
    all_combinations = []

    @classmethod
    def get_bit_combinations(cls, n, arr, i, query_list: list):
        query_list.extend(cls.generate_all_binary_strings(n, arr, i))

    @classmethod
    def generate_all_binary_strings(cls, n, arr, i) -> list:
        x = []
        if i == n:
            s = ''
            bit_sequence = s.join(arr)
            x.append(bit_sequence)
            return x
        # First assign "0" at ith position
        # and try for all other permutations
        # for remaining positions
        arr[i] = "0"

        x.extend(cls.generate_all_binary_strings(n, arr, i + 1))

        # And then assign "1" at ith position
        # and try for all other permutations
        # for remaining positions
        arr[i] = "1"
        x.extend(cls.generate_all_binary_strings(n, arr, i + 1))
        return x