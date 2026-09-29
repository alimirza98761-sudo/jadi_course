name = input("what is your name?")
print(f"hi {name}, my name is Eilym :) ")
'''
اون میفهمه که میخوای ادامه بدی یا نه

 '''
def wants_to_continue():
    answer = input(f"do you want to continue ? ")
    if answer.lower().strip() in ['yes', 'y', 'اره']:
        return True
    else:
        return False
print(wants_to_continue())







