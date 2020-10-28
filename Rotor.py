from random import shuffle


class Rotor:
    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.rotor = list(self.alphabet)

    def shuffle_rotor(self):
        shuffle(self.rotor)
        self.rotor = ''.join(self.rotor)

    def make_pairs_with_alphabet(self):
        pairs = []
        for x, y in zip(self.rotor, self.alphabet):
            pairs.append((x, y))
        self.rotor = pairs

    def __repr__(self):
        output = ''
        for i in range(len(self.rotor)):
            output += f'|{self.rotor[i][0]}-{self.rotor[i][1]}|\n'
        return output
