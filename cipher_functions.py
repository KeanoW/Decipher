from random import sample, shuffle

def create_cipher_key_list(alphabet, phrase_alphabet):
    shuffle(alphabet)
    cipher_key_list = []
    for char in range(len(phrase_alphabet)):
        cipher_key_list.append(alphabet[char])

    return cipher_key_list

def remove_punctuation_marks(phrase):
    phrase_list = list(phrase)
    new_phrase_list = []
    punctuation_list = ('!', ',', '?', '/', '.', ' ')

    for char in phrase_list:
        if char not in punctuation_list:
            new_phrase_list.append(char.lower())

    return new_phrase_list

def get_alphabet_of_phrase(func):
    """
    Pass list of phrase after punctuation removed methode
    """
    set_phrase_alphabet = list(set(func))
    set_phrase_alphabet.sort()

    return set_phrase_alphabet

def create_cipher_phrase(phrase_list, cipher_dict):
    ciphered_phrase = []

    for letter in phrase_list:
        if letter.lower() in cipher_dict.keys():
            ciphered_phrase.append(cipher_dict.get(letter.lower()))
        else:
            ciphered_phrase.append(" ")
    return ciphered_phrase

def changed_dict(ciphered_char, replace_ciphered_char, cipher_dict):
    #create a list to store values where key not equal to value to make sure the value entered doesn't get
    #used for already assigned values
    for k, v in cipher_dict.items():
        if v == ciphered_char:
            if k != v:
                cipher_dict[k] = replace_ciphered_char
    return cipher_dict

def update_cipher(phrase_list, cipher_dict):
    new_ciphered_phrase = []
    for letter in phrase_list:
        if letter == " ":
            new_ciphered_phrase.append(" ")
        else:
            for k, v in cipher_dict.items():
                if letter.lower() == k:
                    new_ciphered_phrase.append(v)
                    continue
    return new_ciphered_phrase

