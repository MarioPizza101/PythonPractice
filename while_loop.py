Menu = '''
     [1] - Name
     [2] - Age
     [3] - Favorite movie
     [4] - Close
'''

def options(option):
    action = True

    if option == "1":
        name = input("Enter you name: ")
        print(f"Your name is {name}.")
    elif option == "2":
        age = input("Enter your age: ")
        print(f"You are {age} years old.")
    elif option == "3":
        movie = input("Enter your favorite movie: ")
        print(f"Your favorite movie is {movie}.")
    elif option == "4":
        action = False
    else:
        print("That is not a valid option")

    return action





status = True
while status:
    print(Menu)
    option = input("Enter an option: ")
    status = options(option)
