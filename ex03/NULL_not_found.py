def NULL_not_found(object: any) -> int:
    try :
        t = type(object)

        def str_func():
            if t is str and len(object) > 1:
                return ("Type not found")
            elif t is str :
                return (f"Empty: {t}")

        ret = {
                float : f'Cheese: nan {t}',
                int: f'Zero: 0 {t}',
                str : str_func(),
                bool : f'Fake: False {t}',
            }
        if object != None:
            print(ret[t])
        else :
            print(f'Nothing: None {t}')
        return 1
    except Exception as e:
        print(e)
        return 2