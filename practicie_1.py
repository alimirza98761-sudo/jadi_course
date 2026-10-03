def begir():
    adad = int(input("ye adad bede :) "))
    return adad

def check_kon(adad):
    if adad == 0:
        return 'true'
    if adad % 2 == 0:
        return 'true'
    else:
        return 'false'

def con():
    txt = input("do you want to continu??? :")
    if txt.upper() in [ 'Y', 'YES', 'ARE']:
        return True
    elif txt.upper() in ['NA', 'N', 'NO']:
        return False
    else:
        print("i don't understand,i think you say False")
        return False

print("Hello dear :) ")
print("welcome, lets play")
while True:
    res = begir()
    print(check_kon(res))
    if not con():
        break
print('good by')