dictionary = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        + "abcdefghijklmnopqrstuvwxyz"
        + "1234567890"
        +",.?!@#$%&*(){}[]:;-_=+ ")

def encrypt(pass_key, shift):
    """ Encrypt pass_key using ceasar algorithm """

    cipher = ""

    for letter in pass_key:
        i = dictionary.index(letter) + shift

        i -= len(dictionary) if i >= len(dictionary) else 0

        cipher += dictionary[i]

    return cipher


def decipher(pass_key, shift):
    """ Decipher pass_key using ceasar algorithm """

    pass
