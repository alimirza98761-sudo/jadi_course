def skyline(*args):
    res = 0
    for x in args:
        if x > res:
            res = x
    return res

print(skyline(3, 7, 15, 2, 9))
         
        