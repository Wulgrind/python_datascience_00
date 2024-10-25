from ft_filter import ft_filter
from sys import argv


def main():
    """Main func"""

    try:
        if len(argv) != 3 or type(argv[1]) is str or type(int(argv[2])) is int:
            raise (AssertionError())
        lst = argv[1].split(' ')
        n = int(argv[2])
        print(ft_filter(lambda x: len(x) > n, lst))
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == '__main__':
    main()