"""
File: caesar.py
Name: Catherine Tsai
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program decodes the ciphered string.
    """
    n = int(input('Secret number: '))
    ciphered_string = str(input("What's the ciphered string? ")).upper()
    print('The deciphered string is: ' + decipher_string(ciphered_string, n))


def decipher_string(ciphered_string, n):
    deciphered_string = ''
    for i in range(len(ALPHABET)):
        ch = ALPHABET[i]
    return deciphered_string


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
