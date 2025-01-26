def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) < 4:
        return ', '.join(x for x in names[:-1]) + f' and {names[-1]}' + ' like this'
    else:
        y = len(names) - 2
        return ', '.join(x for x in names[:2]) + f' and {y} others like this'

print(likes(["Peter", "joe", "jim", "olivia"]))