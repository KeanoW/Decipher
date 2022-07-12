from random import sample

phrase = "Trust in the Lord with all your heart and lean not on your own understanding, in all your ways submit to him"
phrase_list = list(phrase)
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

def create_cipher_key_list(alphabet):
    cipher_key_list = list("".join(sample(alphabet, len(alphabet))))
    return cipher_key_list

cipher_dict = dict(zip(alphabet, create_cipher_key_list(alphabet)))

def create_cipher_phrase(phrase_list, cipher_dict):
    ciphered_phrase = []

    for letter in phrase_list:
        if letter.lower() in cipher_dict.keys():
            ciphered_phrase.append(cipher_dict.get(letter.lower()))
        else:
            ciphered_phrase.append(" ")
    return ciphered_phrase

def changed_dict(ciphered_char, replace_ciphered_char, cipher_dict):
    for k, v in cipher_dict.items():
        if v == ciphered_char:
            if k != v:
                cipher_dict[k] = replace_ciphered_char
        else:
            print("Incorrect Value")
            continue
    return cipher_dict

print(create_cipher_phrase(phrase_list))