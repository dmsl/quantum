from datetime import datetime

from QCLG_lvl3.classical.BitCombinations import BitCombinations


class ClassicalXor:

    @classmethod
    def _super_secret_black_box_function_f(cls, list_of_inputs: list) -> str:
        output_bit = 0
        output_zero = False
        output_one = False
        counts = 0
        for input_bits in list_of_inputs:
            for bit in input_bits:
                output_bit = output_bit ^ int(bit)

            if output_bit == 1:
                output_one = True
            else:
                output_zero = True
            counts = counts + 1
            output_bit = 0
            if output_one and output_zero:
                return f'Balanced After {counts} checks.'
            if counts > (len(list_of_inputs) / 2):
                return f'Constant After {counts} checks.'
        return f'After {counts} checks.'

    @classmethod
    def execute_classical_xor(cls, bits) -> list:
        start = datetime.now()
        inputs = BitCombinations.produce_worse_scenario(BitCombinations.combinations(bits))
        end = datetime.now()
        elapsed = end - start
        time_to_generate_worst_input = elapsed.total_seconds()
        start = datetime.now()
        function_nature = cls._super_secret_black_box_function_f(inputs)
        end = datetime.now()
        elapsed = end - start
        time_str = elapsed.total_seconds()
        final = [time_to_generate_worst_input, time_str, bits, function_nature]
        return final
