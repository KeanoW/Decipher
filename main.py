from random import sample

phrase = "Trust in the Lord with all your heart and lean not on your own understanding, in all your ways submit to him"
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

def create_cipher_key_list(alphabet):
    cipher_key_list = list("".join(sample(alphabet, len(alphabet))))
    return cipher_key_list

cipher_dict = dict(zip(alphabet, create_cipher_key_list(alphabet)))

def remove_punctuation_marks(phrase):
    phrase_list = list(phrase)
    punctuation_dict = {"!": "", ",": "", "?": "", "/": "", ".": ""}

    for i in range(len(phrase_list)):
        for k, v in punctuation_dict.items():
            if phrase_list[i] == k:
                phrase_list[i] == v

    return phrase_list

filtered_phrase_list = remove_punctuation_marks(phrase)

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

ciphered_phrase = create_cipher_phrase(filtered_phrase_list, cipher_dict)
count = 0
modified_ciphered_phrase = []
modified_dict = {}
ciph_char = False
repl_ciph_char = False

while(True):
    if count < 1:
        ciphered_phrase_str = "".join(map(str, ciphered_phrase))
        print(ciphered_phrase_str)
        count = 1

    ciphered_char = input("Character you want to change: ").lower()

    if ciphered_char not in alphabet:
        print("Not Valid character! Try Again")
        ciphered_char = input("Character you want to change: ").lower()
    else:
        ciph_char = True

    replace_ciphered_char = input("New character: ").lower()

    if replace_ciphered_char not in alphabet:
        print("Not Valid character! Try Again")
        replace_ciphered_char = input("New character: ").lower()
    else:
        repl_ciph_char = True

    if ciph_char is True and repl_ciph_char is True:
        modified_dict = changed_dict(ciphered_char, replace_ciphered_char, cipher_dict)
        modified_ciphered_phrase = update_cipher(filtered_phrase_list, modified_dict)

        ciphered_phrase_str = "".join(map(str, modified_ciphered_phrase))
        print(ciphered_phrase_str)

    if modified_dict.values() == alphabet:
        break
        print("Phrase deciphered!")
        print(phrase)
