from sys import argv

try :
    if len(argv) > 2 :
        raise(AssertionError("more than one argument is provided"))
    elif len(argv) == 2:
        try :
            int(argv[1])
        except :
            raise(AssertionError("argument is not an integer"))
        num = int(argv[1])
        res = num % 2
        if res == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    
except Exception as e:
    print(f"AssertionError: {e}")
        