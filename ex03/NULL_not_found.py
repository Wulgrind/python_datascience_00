def NULL_not_found(object: any) -> int:
    try:
        t = type(object)

        def str_func():
            if t is str and len(object) > 1:
                raise ValueError()
            elif t is str:
                return (f"Empty: {t}")

        ret = {
                float: f'Cheese: nan {t}',
                int: f'Zero: 0 {t}',
                str: str_func(),
                bool: f'Fake: False {t}',
            }
        if object is not None:
            print(ret[t])
        else:
            print(f'Nothing: None {t}')
        return 0
    except Exception:
        print("Type not found")
        return 1
