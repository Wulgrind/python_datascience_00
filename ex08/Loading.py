def ft_tqdm(lst: range) -> None:
    """ft_tqdm replica"""
    bar_display = ' ' * 60 + '>'
    for i in lst:
        progress = ">"
        prc = int((i * 100) / len(lst))
        last = 0
        for j in range(60):
            if int((j * 100) / 60) == prc and j > last:
                last = j + 1
                bar_display = ('=' * last) + ' ' * (60 - last) + '>'
        ret = f"\r{prc + 1}%|[{bar_display}]| {i + 1}/{len(lst)}"
        print(ret, end='', flush="True")
        progress = "=" + progress
        yield i

if __name__ == '__main__':
    pass