from hashlib import sha256
from numpy.random import randint


alphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            + "abcdefghijklmnopqrstuvwxyz"
            + "1234567890"
            +",.?!@#$%&*(){}[]:;-_=+ ")


def check_password(pss_key):
    """ Check master password be correct """

    pss_hash = ('52120eb30a3aba0c70b2a7e0db51bd539'
                + '69d7ca40f1653f7c110fb49b3e3c221')

    new_hash = sha256(pss_key.encode('utf-8')).hexdigest()

    return bool(new_hash == pss_hash)


def create_pass_key():
    """
        Generate a password with 16 characters
            selected randomly from alphabet
    """

    index = randint(0, len(alphabet), 32)

    while (index[-1] == alphabet.index(" ")
           or index[0] == alphabet.index(" ")):

        index = randint(0, len(alphabet), 32)

    pass_key = ""
    for i in index:
        pass_key += alphabet[i]

    return pass_key
