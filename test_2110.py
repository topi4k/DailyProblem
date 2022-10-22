def crazyfunction(L, n):
    dc = {L[0]: 0}
    result = False
    tupleSol = 0, 0
    for k in L:
        complement = n - k
        if complement in dc.keys():
            dc[complement] = k
            result = True
            tupleSol = k, complement
            break
        else:
            dc[k] = 0
    return result, tupleSol


print(crazyfunction([1, 2, 3, 4], 7))
