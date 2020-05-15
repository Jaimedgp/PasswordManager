"""
    Module with all the functions related to passwords or
    private key used to sign into the database

    @author Jaimedgp
    @date May, 2020
"""

from hashlib import sha256
from numpy.random import randint
from KyManager.encrypt.rsa import Rsa


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


def create_pass_key(key_size):
    """ Generate a password with key_size characters
               selected randomly from ALPHABET       """


    index = randint(0, len(ALPHABET), key_size)

    while (index[-1] == ALPHABET.index(" ")
           or index[0] == ALPHABET.index(" ")):

        index = randint(0, len(ALPHABET), key_size)

    pass_key = "".join([ALPHABET[i] for i in index])

    return pass_key


def check_private_key(private_key, master_hash):
    """ Check if private key is correct """

    key_hash = sha256(private_key).hexdigest()

    return bool(key_hash == master_hash)


def init_rsa(key_size, key_file, database):
    """ Initialize RSA keys storing its hash in the
        database and the private key in a file      """

    # Create the private Key
    rsa = Rsa(key_size=key_size)

    # save private key hash into the database
    key_hash = sha256(rsa.private_key).hexdigest()
    database.connect.execute("""
            INSERT INTO PASS_KEY(pass_key, service, account)
                VALUES ('{0}', 'Master', 'Master');
            """.format(key_hash))
    database.connect.commit()

    # Save private key into a file
    with open(key_file, 'w') as file:
        file.write(rsa.export_private_key())

    return rsa
