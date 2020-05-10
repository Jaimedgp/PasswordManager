alphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            + "abcdefghijklmnopqrstuvwxyz"
            + "1234567890"
            +",.?!@#$%&*(){}[]:;-_=+ ")


def encrypt(pass_key, subkey):
    """ Encrypt pass_key using Vignere algorithm """

    cipher = ""

    for pk_letter, sk_letter in zip(pass_key, subkey):
        pk_i = alphabet.index(pk_letter)
        sk_i = alphabet.index(sk_letter)

        new_i = (pk_i + sk_i) % len(alphabet)
        cipher += alphabet[new_i]

    return cipher


def decipher(pass_key, subkey):
    """ Decipher pass_key using Vignere algorithm """

    cipher = ""

    for pk_letter, sk_letter in zip(pass_key, subkey):
        pk_i = alphabet.index(pk_letter)
        sk_i = alphabet.index(sk_letter)

        new_i = (pk_i - sk_i) % len(alphabet)
        cipher += alphabet[new_i]

    return cipher
