def pick_evens(*args):
    res = []
    for x in args:
        if x % 2 ==0:
            res.append(x)
    return res

print(pick_evens(1,2,8,9,6,43,0,5))