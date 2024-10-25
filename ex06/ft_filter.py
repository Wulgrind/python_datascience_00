def ft_filter(fnc, obj):
    """filter(function or None, iterable) --> filter object

    Return an iterator yielding those items
    of iterable for which function(item)
    is true. If function is None, return the items that are true."""

    ret = [x for x in obj if fnc(x)]
    return (ret)


if __name__ == '__main__':
    pass
