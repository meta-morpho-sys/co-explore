

def c2i(c):
    """ Converts alphabet character c (in the range a-z)
    into an integer in the range 0-25.

    Note: This is the inverse operation of i2c.
    """
    char_code = ord(c)
    result = char_code - ord('a')
    return result


def i2c(i):
    """ Converts integer i (in the range 0-25) into the
    corresponding letter of the alphabet a-z.

    Note: This is the inverse operation of c2i.
    """
    char_num = i + ord('a')
    return chr(char_num)


def rot13(c):
    """ ROT13 cipher. 'Rotates' character c by 13 steps in the alphabet.
    """
    code = c2i(c)
    rotated_code = (code + 13) % 26
    result = i2c(rotated_code)
    return result


plaintext = raw_input('Enter a secret message: ')
for c in plaintext:
    print(rot13(c))


