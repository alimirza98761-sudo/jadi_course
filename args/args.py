def jam_hoomand(*args):
    total = 0
    count = 0
    for x in args:
        if x > 0:
            total += x
            count += 1
       
    return count, total

print(jam_hoomand(5, -2, 3, -10, 4))


