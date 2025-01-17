from sys import argv


def main():
    """My main func"""
    try:
        ret = ""
        nested_morse = {
            ' ': '/',
            'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '0': '-----',
        }
        if len(argv) != 2:
            raise (AssertionError())
        for i in argv[1]:
            if i.isalpha():
                i = i.upper()
            if not i in nested_morse:
                    raise (AssertionError())
            if i.isdigit():
                ret += nested_morse[i] + ' '
            else:
                ret += nested_morse[i] + ' '
        ret = ret[:len(ret) - 1]
        print(ret)

    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == '__main__':
    main()
