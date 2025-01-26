def tribonacci(signature, n):
    res = []
    if n == 0:
        return res
    for i in range(n):
        if i < 3:
            res.append(signature[i])
        else:
            res.append(res[i-3] + res[i-2] + res[i-1])
    return res

sig = [1, 1, 1]
print(tribonacci(sig, 10))