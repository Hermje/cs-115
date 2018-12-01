#Author: Jake Herman
#Section: C
#Description: this program can either decode or encode phrases using a rot 13 cipher strategy

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#when cipher alphabet is created it is formatted into a dictionary for really simple lookup when encoding/decoding
cipher_dict = {}

def make_cipher_alphabet(start_char):
    cipher_alphabet = []
    #keeps track of how many times the alphabet is iterated thru, probably a better way to do this...
    count = 0
    #goes thru the alphabet multiple times so we can rotate around the starting character
    while count < 2:
        for char in alphabet:
            if char == start_char:
                #we are back where we started
                count += 1

            if count == 1:
                cipher_alphabet.append(char)
    #moves the second half to the front to put the starting character in the middle
    cipher_alphabet = cipher_alphabet[13:26] + cipher_alphabet[0:13]
    #compares new cipher alphabet to english alphabet for debugging purposes
    print("Plain alphabet: {}".format("".join(alphabet)))
    print("Cipher alphabet: {}".format("".join(cipher_alphabet)))
    #turns cipher alphabet list into a dictionary so encoding/decoding is simple syntax-wise
    for idx, char in enumerate(alphabet):
        cipher_dict[char] = cipher_alphabet[idx]

#takes in a string that is an english word to be encoded
def encode_phrase(phrase):
    encoded_phrase = []
    for char in phrase.lower():
        #a KeyError is thrown when a non-alpha character is being encoded
        #such as spaces or punctuation, those do not need to be encoded so we just skip over it
        try:
            #takes in the character from the english word and looks up the rot 13 equivalent
            #it is then appended to the encoded phrase list containing the rest of the rot 13 characters
            encoded_phrase.append(cipher_dict[char])
        except KeyError:
            #the current character is non alpha, doesn't need to be encoded, and can simply be appended to the list
            encoded_phrase.append(char)
            #continue so program doesn't terminate
            continue
    #the encoded phrase is a list.
    #here, all characters in the list are joined together and returned
    return "".join(encoded_phrase)

#takes in a string that is a rot 13 encoded word to be translated back into english
def decode_phrase(phrase):
    decoded_phrase = []
    #inverts the rot13 cipher dictionary for simple decoding
    decipher_dict = {v: k for k, v in cipher_dict.items()}

    #looks up by key (reverse), works because no letter corresponds to the same key
    for char in phrase.lower():
        #same keyerror handling for same reason as encoding
        try:
            decoded_phrase.append(decipher_dict[char])
        except KeyError:
            decoded_phrase.append(char)
            continue

    return "".join(decoded_phrase)

def prompt():
    make_cipher_alphabet(str(input("enter the starting character:")))
    choice = str(input("would you like to (e)ncode or (d)ecode? Enter q to quit. "))

    return choice

while True:
    choice = prompt()

    if choice.lower() == 'e':
        print(encode_phrase(str(input("enter the phrase you'd like to encode: "))))
    elif choice.lower() == 'd':
        print(decode_phrase(str(input("enter the phrase you'd like to decode: "))))
    else:
        break
