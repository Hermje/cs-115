#Author: Jake Herman
#Section: C
#Description: this program can either decode or encode phrases using a rot 13 cipher strategy

#TODO: handle spaces and other characters

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#when cipher alphabet is created it is formatted into a dictionary for really simple lookup when encoding/decoding
cipher_dict = {}

def make_cipher_alphabet(start_char):
    start_idx = 0
    cipher_alphabet = []
    #finds the index in our alphabet list that is the users prefferred starting character
    for idx, char in enumerate(alphabet):
        if char == start_char.lower():
            start_idx = idx

    count = 0
    #goes thru the alphabet multiple times so we can rotate around the starting character
    while count < 2:
        for idx, char in enumerate(alphabet):
            if char == start_char:
                count += 1

            if count == 1:
                cipher_alphabet.append(char)
    #moves the second half to the front to put the starting character in the middle
    cipher_alphabet = cipher_alphabet[13:26] + cipher_alphabet[0:13]
    print("Plain alphabet: {}".format("".join(alphabet)))
    print("Cipher alphabet: {}".format("".join(cipher_alphabet)))
    #turns cipher alphabet list into a dictionary so encoding/decoding is simple syntax-wise
    for idx, char in enumerate(alphabet):
        cipher_dict[char] = cipher_alphabet[idx]

def encode_phrase(phrase):
    encoded_phrase = []
    for char in phrase:
        encoded_phrase.append(cipher_dict[char])

    return "".join(encoded_phrase)

def decode_phrase(phrase):
    decoded_phrase = []
    #looks up by key (reverse), works because no letter corresponds to the same key
    for char in phrase:
        for decoded_char, encoded_char in cipher_dict.items():
            if char == encoded_char:
                decoded_phrase.append(decoded_char)

    return "".join(decoded_phrase)

make_cipher_alphabet(str(input("starting character:")))

choice = str(input("would you like to (e)ncode or (d)ecode? enter q to quit "))

if choice.lower() == 'e':
    print(encode_phrase(str(input("enter the phrase you'd like to encode: "))))
elif choice.lower() == 'd':
    print(decode_phrase(str(input("enter the phrase you'd like to decode: "))))
