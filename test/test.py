import unittest
import string
from Enigma import Enigma


class TestEnigma(unittest.TestCase):

    def setUp(self):
        alphabet = string.ascii_uppercase
        rotors = [
            {0: 4, 1: 10, 2: 12, 3: 5, 4: 11, 5: 6, 6: 3, 7: 16, 8: 21, 9: 25, 10: 13, 11: 19, 12: 14, 13: 22, 14: 24,
             15: 7, 16: 23, 17: 20, 18: 18, 19: 15, 20: 0, 21: 8, 22: 1, 23: 17, 24: 2, 25: 9},
            {0: 0, 1: 9, 2: 3, 3: 10, 4: 18, 5: 8, 6: 17, 7: 20, 8: 23, 9: 1, 10: 11, 11: 7, 12: 22, 13: 19, 14: 12,
             15: 2, 16: 16, 17: 6, 18: 25, 19: 13, 20: 15, 21: 24, 22: 5, 23: 21, 24: 14, 25: 4},
            {0: 1, 1: 3, 2: 5, 3: 7, 4: 9, 5: 11, 6: 2, 7: 15, 8: 17, 9: 19, 10: 23, 11: 21, 12: 25, 13: 13, 14: 24,
             15: 4, 16: 8, 17: 22, 18: 6, 19: 0, 20: 10, 21: 12, 22: 20, 23: 18, 24: 16, 25: 14}]
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
        code = []
        self.enigma = Enigma(rotors, reflector, alphabet, code)

    def test_should_return_000_when_rotors_keys_zzz(self):
        self.enigma.keys = [25, 25, 25]
        self.enigma.spin_rotor()
        self.assertEqual(self.enigma.keys, [0, 0, 0])

    def test_should_return_010_when_rotors_keys_zaa(self):
        self.enigma.keys = [25, 0, 0]
        self.enigma.spin_rotor()
        self.assertEqual(self.enigma.keys, [0, 1, 0])

    def test_should_return_100_when_rotors_keys_aaa(self):
        self.enigma.keys = [0, 0, 0]
        self.enigma.spin_rotor()
        self.assertEqual(self.enigma.keys, [1, 0, 0])

    def test_should_return_001_when_rotors_keys_zza(self):
        self.enigma.keys = [25, 25, 0]
        self.enigma.spin_rotor()
        self.assertEqual(self.enigma.keys, [0, 0, 1])

    def test_should_return_034_when_rotors_keys_zce(self):
        self.enigma.keys = [25, 2, 4]
        self.enigma.spin_rotor()
        self.assertEqual(self.enigma.keys, [0, 3, 4])

    def test_should_return_encoded_W_when_a_is_given_and_qvc_as_a_keys(self):
        self.enigma.keys = [16, 21, 2]
        actual = self.enigma.encode_message('a')
        expected = 'W'
        self.assertEqual(actual, expected)

    def test_should_return_decoded_A_when_w_is_given_and_qvc_as_a_keys(self):
        self.enigma.keys = [16, 21, 2]
        actual = self.enigma.encode_message('w')
        expected = 'A'
        self.assertEqual(actual, expected)
