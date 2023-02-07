""" https://en.wikipedia.org/wiki/Atbash """
import string

def atbash(sequence: str) -> str:
    """
    >>> atbash("ABCDEFG")
    'ZYXWVUT'

    >>> atbash("aW;;123BX")
    'zD;;123YC'
    """
    letters = string.ascii_letters
    letters_reversed = string.ascii_lowercase[::-1] + string.ascii_uppercase[::-1]
    return "".join(
        letters_reversed[letters.index(c)] if c in letters else c for c in sequence
    )



if __name__ == "__main__":
    Texto_encriptado = 'GSVUOZTRHHZBDVZIVXIZAB'
    print(f'Texto encriptado: {Texto_encriptado}')
    print(f'Texto desencriptado: {atbash(Texto_encriptado)}')


# Codigo sacado de https://the-algorithms.com/es/algorithm/atbash
