l = [1, 2, 'a', 'b']


def filter_list(l):
    filtered = []
    [filtered.append(x) for x in l if type(x) is not str]
    return filtered

print(filter_list(l))