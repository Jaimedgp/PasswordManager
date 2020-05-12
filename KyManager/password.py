"""
    Module with all the functions related to passwords or
    private key used to sign into the database

    @author Jaimedgp
    @date May, 2020
"""

from hashlib import sha256
from numpy.random import randint


ALPHABET = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            + "abcdefghijklmnopqrstuvwxyz"
            + "1234567890"
            +",.?!@#$%&*(){}[]:;-_=+ ")


def check_password(pss_key):
    """ Check master password be correct """

    pss_hash = ('52120eb30a3aba0c70b2a7e0db51bd539'
                + '69d7ca40f1653f7c110fb49b3e3c221')

    new_hash = sha256(pss_key.encode('utf-8')).hexdigest()

    return bool(new_hash == pss_hash)


def check_private_key(private_file, master_hash):
    """ Check if private key is correct """

    private_key = open(private_file, "r").read()
    key_hash = sha256(private_key.encode('utf-8')).hexdigest()

    return bool(key_hash == master_hash)


def create_pass_key():
    """ Generate a password with 16 characters
          selected randomly from ALPHABET     """


    index = randint(0, len(ALPHABET), 32)

    while (index[-1] == ALPHABET.index(" ")
           or index[0] == ALPHABET.index(" ")):

        index = randint(0, len(ALPHABET), 32)

    pass_key = ""
    for i in index:
        pass_key += ALPHABET[i]

    return pass_key
