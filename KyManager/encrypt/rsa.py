"""
    Module file with encryptation class using RSA method

    @author Jaimedgp
    @date May, 2020
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5
from Crypto import Random

class Rsa():
    """ RSA class to manage all rsa methods """

    def __init__(self, private_key=None, key_size=0, key_file=None):
        """ Initialize Rsa object by a private key or creating a new one
            by its key_size or importing an existing one from a key_file """

        if private_key is not None:
            self.import_private_key(private_key)
        if key_file is not None:
            self.import_from_file(key_file)
        elif key_size > 0:
            self.get_new_key(key_size)

        self.public_key = self.private_key.publickey()


    def get_new_key(self, key_size):
        """ Create a new private key """

        random_generator = Random.new().read
        self.private_key = RSA.generate(key_size, random_generator)


    def import_private_key(self, private_key):
        """ Import an existing private key """

        self.private_key = RSA.importKey(private_key)


    def import_from_file(self, key_file):
        """ Import private key from a file """

        key = open(key_file, 'r').read()

        self.private_key = RSA.importKey(key.encode('utf-8'))


    def export_private_key(self):
        """ Export private key decoding in utf-8 code """

        return self.private_key.exportKey().decode('utf-8')


    def encrypt(self, message):
        """ Encrypt message using the public key """

        cipher = PKCS1_OAEP.new(self.public_key)
        return cipher.encrypt(message.encode('utf-8'))


    def decrypt(self, ciphertext):
        """ Decrypt a ciphertext using the private key """

        cipher = PKCS1_OAEP.new(self.private_key)
        return cipher.decrypt(ciphertext).decode('utf-8')


    def sign(self, message, hash_alg="SHA-256"):
        """ Sign a message with the private key """

        signer = PKCS1_v1_5.new(self.private_key)

        if hash_alg == "SHA-512":
            digest = SHA512.new()
        elif hash_alg == "SHA-384":
            digest = SHA384.new()
        elif hash_alg == "SHA-256":
            digest = SHA256.new()
        elif hash_alg == "SHA-1":
            digest = SHA.new()
        else:
            digest = MD5.new()

        digest.update(message)
        return signer.sign(digest)


    def verify(self, message, signature, hash_alg="SHA-256"):
        """ Verify the signature of a message using public key """

        signer = PKCS1_v1_5.new(self.public_key)

        if hash_alg == "SHA-512":
            digest = SHA512.new()
        elif hash_alg == "SHA-384":
            digest = SHA384.new()
        elif hash_alg == "SHA-256":
            digest = SHA256.new()
        elif hash_alg == "SHA-1":
            digest = SHA.new()
        else:
            digest = MD5.new()

        digest.update(message)
        return signer.verify(digest, signature)


    def get_private_key(self):
        """ Get the private key by calculate the hash """

        return self.export_private_key().encode('utf-8')
