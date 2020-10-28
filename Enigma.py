class Enigma:
    def __init__(self, rotors, reflector, alphabet, code):
        self.rotors = rotors
        self.reflector = reflector
        self.alphabet = alphabet
        self.keys = [alphabet.index(x.upper()) for x in code]

    def __repr__(self):
        output = ''
        rotors_list = [[(x, y) for x, y in rotor.items()] for rotor in self.rotors]
        for pair, i in zip(self.reflector.items(), range(len(self.alphabet))):
            output += f'|{pair[0]}{pair[1]}|\t'
            for rotor in rotors_list:
                output += f'|{self.alphabet[rotor[i][0]]}-{self.alphabet[rotor[i][1]]}| \t'
            output += '\n'
        return output

    def encode_message(self, message):
        encoded_message = ''
        message = [ord(char) - 65 for char in message.upper()]
        for letter in message:
            self.spin_rotor()
            letter_in_first_rotor = (letter + self.keys[0]) % len(self.alphabet)
            pair_for_first_rotor = self.rotors[0].get(letter_in_first_rotor)

            key_index = 1
            reflectors_letter = self.__from_right_to_left(pair_for_first_rotor, key_index)
            reflectors_letter = self.reflector.get(self.alphabet[reflectors_letter])
            reflectors_letter = self.alphabet.index(reflectors_letter)

            letter_in_last_rotor = (reflectors_letter + self.keys[-1]) % len(self.alphabet)
            pair_for_last_rotor = self.__get_key(letter_in_last_rotor, -1)
            key_index = len(self.rotors) - 2
            final_letter = self.__from_left_to_right(pair_for_last_rotor, key_index)
            encoded_message += self.alphabet[final_letter]
        return encoded_message

    def decode_message(self, message, code):
        self.keys = [self.alphabet.index(x.upper()) for x in code]
        decoded_message = self.encode_message(message)
        return decoded_message

    def spin_rotor(self):
        i = 0
        while self.keys[i] + 1 >= len(self.alphabet):
            self.keys[i] = 0
            i += 1
            if i >= len(self.keys):
                break
        else:
            self.keys[i] += 1

    def __from_right_to_left(self, letter, current):
        if current == len(self.rotors):
            return (letter - self.keys[-1]) % len(self.alphabet)
        prev = current - 1
        reflectors_letter = (letter + (self.keys[current] - self.keys[prev])) % len(self.alphabet)
        return self.__from_right_to_left(self.rotors[current].get(reflectors_letter), current + 1)

    def __from_left_to_right(self, letter, current):
        if current == -1:
            return (letter - self.keys[0]) % len(self.alphabet)
        prev = current + 1
        new_letter = (letter - (self.keys[prev] - self.keys[current])) % len(self.alphabet)
        return self.__from_left_to_right(self.__get_key(new_letter, current), current - 1)

    def __get_key(self, value, index):
        for k, v in self.rotors[index].items():
            if v == value:
                return k
