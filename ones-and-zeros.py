def binary_array_to_number(arr):
    res = 0
    pow = 0
    for num in reversed(arr):
        res += num*(2**pow)
        pow += 1
    return res


print(binary_array_to_number([1, 1, 1, 1]))