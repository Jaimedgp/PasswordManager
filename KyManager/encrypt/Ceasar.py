alphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            + "abcdefghijklmnopqrstuvwxyz"
            + "1234567890"
            +",.?!@#$%&*(){}[]:;-_=+ ")


def encrypt(pass_key, shift):
    """ Encrypt pass_key using ceasar algorithm """

    cipher = ""

    for letter in pass_key:
        i = alphabet.index(letter) + shift

        i -= len(alphabet) if i >= len(alphabet) else 0

        cipher += alphabet[i]

    return cipher


def decipher(pass_key, shift):
    """ Decipher pass_key using ceasar algorithm """

    cipher = ""

    for letter in pass_key:
        i = alphabet.index(letter) - shift

        i -= len(alphabet) if i >= len(alphabet) else 0

        cipher += alphabet[i]

    return cipher
