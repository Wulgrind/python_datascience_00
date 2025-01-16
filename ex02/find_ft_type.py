def all_thing_is_obj(object: any) -> int:
    t = type(object)

    def str_func():
        if t is str and 'Brian' in object:
            return (f"Brian is in the kitchen : {t}")
        elif t is str and 'Toto' in object:
            return (f"Toto is in the kitchen : {t}")

    ret = {
            list: f'List : {t}',
            tuple: f'Tuple : {t}',
            set: f'Set : {t}',
            dict: f'Dict : {t}',
            str: str_func(),
            int: 'Type not found'
        }

    print(ret[t])
    return 42
