def begir():
    adad = int(input("ye adad bede :) "))
    return adad

def check_kon(adad):
    if adad == 0:
        return True
    if adad % 2 == 0:
        return True
    else:
        return False

print("Hello dear :) ")
print("welcome, lets play")
res = begir()
print(check_kon(res))
