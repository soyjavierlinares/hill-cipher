#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# --- IMPLEMENTATION GOES HERE -----------------------------------------------
#  Student helpers (functions, constants, etc.) can be defined here, if needed
import numpy as np

VALID_CHARACTERS = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                             '.', ',', ':', '?', ' '])


def get_position(char):
    # Uppercase the char
    char = char.upper()
    # get the position in the array
    position = np.where(VALID_CHARACTERS == char)[0]
    if len(position) > 0:
        return position[0]
    else:
        return -1


def split_array(array, size):
    new_array = []
    temporal_array = []
    for value in array:
        temporal_array.append(value)
        if len(temporal_array) >= size:
            new_array.append(temporal_array)
            temporal_array = []
    if len(temporal_array)> 0:
        new_array.append(temporal_array)
    return new_array


# ----------------------------------------------------------------------------


def uoc_hill_genkey(size):
    """
    EXERCISE 1: Hill Key Generation
    :size: matrix size
    :return: size x size matrix containing the key
    """

    # --- IMPLEMENTATION GOES HERE ---
    matrix = np.random.randint(len(VALID_CHARACTERS), size=(size, size))
    # --------------------------------

    return matrix


def uoc_hill_cipher(message, key):
    """
    EXERCISE 2: Hill cipher
    :message: message to cipher (plaintext)
    :key: key to use when ciphering the message (as it is returned by 
          uoc_hill_genkey() )
    :return: ciphered text
    """

    ciphertext = ""

    # --- IMPLEMENTATION GOES HERE ---

    message_values = []
    for char in message:
        value = get_position(char)
        message_values.append(value)

    splited_array = split_array(message_values, len(key))

    for group in splited_array:

        if len(group) < len(key):
            while len(group) < len(key):
                group=np.append(group, get_position('X'))

        new_values = np.dot(key, group) % len(VALID_CHARACTERS)

        for value in new_values:
            ciphertext = ciphertext + VALID_CHARACTERS[value]

    # --------------------------------

    return ciphertext


def uoc_hill_decipher(message, key):
    """
    EXERCISE 3: Hill decipher
    :message: message to decipher (ciphertext)
    :key: key to use when deciphering the message (as it is returned by 
          uoc_hill_genkey() )
    :return: plaintext corresponding to the ciphertext
    """

    plaintext = ""

    # --- IMPLEMENTATION GOES HERE ---

    # --------------------------------

    return plaintext


if __name__ == '__main__':
    key = [[5, 15, 18, 15, 10], [22, 10, 35, 10, 37], [28, 33, 31, 7, 30], [14, 35, 33, 38, 28], [30, 0, 37, 26, 6]]
    plaintext = "ONE, TWO OR THREE?"
    ciphertext = "VJ03HX,OH?5G7OVE6IID"
    result = uoc_hill_cipher(plaintext, key)
    print('Esperado: ', ciphertext)
    print('Resultado: ', result)
