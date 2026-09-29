def greet(name):
    return (f"hi {name}, my name is Eilym :) ")
'''
اون میفهمه که میخوای ادامه بدی یا نه

 '''
def wants_to_continue():
    answer = input(f"do you want to continue ? ")
    if answer.lower().strip() in ['yes', 'y', 'اره']:
        return True
    else:
        return False
while True:
    name = input("what is your name ? ")
    print(greet(name))
    if not wants_to_continue():
        print("i'm sorry to hear that;good luck")
        break