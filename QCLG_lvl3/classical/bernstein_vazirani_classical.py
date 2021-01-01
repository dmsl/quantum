class BersteinVaziraniClassical:

    @classmethod
    def guess_number(cls, secret_binary):
        mask = 1
        guess = ""
        attempts = 0
        for bit in secret_binary:
            hit = int(bit) & mask
            guess += str(hit)
            attempts += 1
        return f"My guess After {attempts} attempts is:\n{guess}."
