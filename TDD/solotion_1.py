def divide(a, b):
    result = a / b
    return result

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

except ValueError:
    print("please type int")
except ZeroDivisionError :
    print("you can't use 0 for num2 ")
else:
    print("The program executed successfully")

print("Result:", divide(num1, num2))



    



























