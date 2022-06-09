def uniqueElement(arr, n):
    res = 0
    for i in arr:
        res ^= i
    return res
