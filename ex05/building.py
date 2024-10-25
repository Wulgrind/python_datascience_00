from sys import argv


def main():
    """This is my main func, used to  do the ex05"""
    try:
        digits_list = '0123456789'
        puncts_list = ';.!,?-'
        arg = ""
        if len(argv) < 2 or len(argv[1]) < 1:
            while len(arg) < 1:
                arg = input("Please provide a valid string.\n")
        elif len(argv) > 2:
            raise (AssertionError("Only one argument is accepted."))
        else:
            arg = argv[1]
        upper = 0
        lower = 0
        punc = 0
        digits = 0
        spaces = arg.count(' ') + arg.count('\r')
        for i in arg:
            if i.isupper():
                upper += 1
            if i.islower():
                lower += 1
            if i in puncts_list:
                punc += 1
            if i in digits_list:
                digits += 1
        spaces = arg.count(' ')
        print(f"The text contains {len(arg)} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punc} punctuation marks")
        print(f"{spaces} spaces")
        print(f"{digits} digits")
    except Exception as e:
        print(f"AssertionError: {e}")


if __name__ == '__main__':
    main()
