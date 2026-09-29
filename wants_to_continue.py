print(f"hi my name is Eilym :) ")
def wants_to_continue():
    answer = input(f"do you want to continue ? ")
    if answer.lower().strip() in ['yes', 'y', 'are']:
        return True
    else:
        return False
print(wants_to_continue())







