alphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            + "abcdefghijklmnopqrstuvwxyz"
            + "1234567890"
            +",.?!@#$%&*(){}[]:;-_=+ ")


def encrypt(pass_key, key):
    """ Encrypt pass_key using multiplicative algorithm """

    cipher = ""

    for letter in pass_key:
        i = alphabet.index(letter)
        new_i = (i*key) % len(alphabet)

        cipher += alphabet[new_i]

    return cipher


def decipher(pass_key, key):
    """ Decipher pass_key using multiplicative algorithm """

    pass
