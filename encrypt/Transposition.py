import numpy as np

def encrypt(pass_key, width):
    """ Encrypt pass_key using transposition algorithm """

    numRows = int(len(pass_key) / width + 0.5)

    characters = [letter for letter in pass_key]
    while len(characters) < width*numRows:
        characters.append("<")

    board = np.array(characters).reshape((numRows, width))
    print(board)
    cipher = "".join(["".join(board[:, i]) for i in range(width)])

    return cipher


def decipher(pass_key, width):
    """ Decipher pass_key using transposition algorithm """

    pass
