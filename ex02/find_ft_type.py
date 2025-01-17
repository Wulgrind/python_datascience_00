def all_thing_is_obj(object: any) -> int:
    t = type(object)
    ret = {
        list: f'List : {t}',
        tuple: f'Tuple : {t}',
        set: f'Set : {t}',
        dict: f'Dict : {t}',
        str: f'{object} is in the kitchen : {t}',
        int: 'Type not found',
        float: 'Type not found'
    }

    print(ret[t])
    return 42
