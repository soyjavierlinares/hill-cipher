# HILL CIPHER
Code developed within the subject of cryptography at the Universitat Oberta de Cataluña. In it you will find a way to generate keys to encrypt clear text following Hill chiper method, a function to encrypt clear text and a function to decrypt ciphertext.

## Built with 🛠️

* [Numpy](https://numpy.org/) is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
* [SymPy](https://www.sympy.org/en/index.html) is a library written in Python whose objective is to gather all the characteristics of a computer algebra system (CAS), to be easily extensible and to keep the code as simple as possible.
## Summary 📌

### *Configuration constants*
In the constant `VALID_CHARACTERS` it is configured which characters can be encrypted and its position in the array is used to assign them a value.
On the other hand, the constant `PADDING` is used to add an extra character when the Hill cipher requires it.
```python
VALID_CHARACTERS = np.array(['A', 'B', 'C', ...])

PADDING = 'X'
```
### *Helpers*
The `get_position` function returns the position of a character in the array.
```python
def get_position(char):
    char = char.upper()
    position = np.where(VALID_CHARACTERS == char)[0]
    if len(position) > 0:
        return position[0]
    else:
        return -1
```
The `split_array` function splits an array according to size, the last chunk can be smaller than the given size.
```python
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
```
The `get_inverse_key` function returns the inverse matrix of the key. This inverse matrix is used for decryption of ciphertext.
```python
def get_inverse_key(key):
    matrix = sympy.Matrix(key)
    inv_matrix = matrix.inv_mod(len(VALID_CHARACTERS))
    return np.array(inv_matrix).astype(np.int64)
```
### *Main functions*
The `uoc_hill_genkey` function generates a size x size matrix with random numbers between 0 and the total of valid characters.
```python
def uoc_hill_genkey(size):
    matrix = np.random.randint(len(VALID_CHARACTERS), size=(size, size))
    return matrix
```
The `uoc_hill_cipher`function encrypt given a clear text and a key generated by `uoc_hill_genkey`.
```python
def uoc_hill_cipher(message, key):

    ciphertext = ""

    message_values = []
    for char in message:
        value = get_position(char)
        message_values.append(value)

    splited_array = split_array(message_values, len(key))

    for group in splited_array:

        if len(group) < len(key):
            while len(group) < len(key):
                group=np.append(group, get_position(PADDING))

        new_values = np.dot(key, group) % len(VALID_CHARACTERS)

        for value in new_values:
            ciphertext = ciphertext + VALID_CHARACTERS[value]

    return ciphertext
```
The `uoc_hill_decipher` function decrypts given a ciphertext and the key that was used to encrypt it.
```python
def uoc_hill_decipher(message, key):

    plaintext = ""

    invers_key = get_inverse_key(key)

    message_values = []
    for char in message:
        value = get_position(char)
        message_values.append(value)

    splited_array = split_array(message_values, len(invers_key))

    for group in splited_array:

        if len(group) < len(invers_key):
            while len(group) < len(invers_key):
                group=np.append(group, get_position(PADDING))

        new_values = np.dot(invers_key, group) % len(VALID_CHARACTERS)
        for value in new_values:
            plaintext = plaintext + VALID_CHARACTERS[int(value)]

    while plaintext[len(plaintext)-1] == PADDING:
        plaintext= plaintext[0:len(plaintext)-1]

    return plaintext
```
## Author ✒️
**Javier Linares** - [soyjavierlinares](https://github.com/soyjavierlinares)
