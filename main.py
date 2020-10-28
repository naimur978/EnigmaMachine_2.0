import string
from random import shuffle
from Enigma import Enigma


def get_rotors(count):
    return [[x for x in range(len(alphabet))] for _ in range(count)]


def shuffle_rotors(rotors):
    for rotor in rotors:
        shuffle(rotor)


def make_pairs_with_alphabet(rotors):
    return [{y: x for x, y in zip(rotor, range(len(alphabet)))} for rotor in rotors]


alphabet = string.ascii_uppercase
reflector = {
    'Y': 'A',
    'R': 'B',
    'U': 'C',
    'H': 'D',
    'Q': 'E',
    'S': 'F',
    'L': 'G',
    'D': 'H',
    'P': 'I',
    'X': 'J',
    'N': 'K',
    'G': 'L',
    'O': 'M',
    'K': 'N',
    'M': 'O',
    'I': 'P',
    'E': 'Q',
    'B': 'R',
    'F': 'S',
    'Z': 'T',
    'C': 'U',
    'W': 'V',
    'V': 'W',
    'J': 'X',
    'A': 'Y',
    'T': 'Z'
}
count_of_rotors = int(input("Enter count of rotors : "))
rotors = get_rotors(count_of_rotors)
shuffle_rotors(rotors)
rotors = make_pairs_with_alphabet(rotors)
keys = input(f"Enter {count_of_rotors} key(s) with space : ").split()
enigma = Enigma(rotors, reflector, alphabet, keys)
print(enigma)
message = input("Enter your message : ")

encoded_message = enigma.encode_message(message)
print(f'Your encoded message: {encoded_message}')

decoded_message = input("Enter encoded message : ")
keys = input(f"Enter {count_of_rotors} key(s) with space : ").split()
decoded_message = enigma.decode_message(decoded_message, keys)
print(f'Your decoded message: {decoded_message}')
