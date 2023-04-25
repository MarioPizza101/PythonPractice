family = ["Alex" , "Michelle" , "Amy" , "Michel" , "Mercury"]

nameAmy = 47
nameMichel = 46
nameAlex = 16
nameMichelle = 14
nameMax = 5

family_name = "thomatis"
family_size = len(family)


if family_name == "thomatis" or family_size == 4:
    print("you are in my family")
elif family_name == "fritts":
    print("you are not in my family")
else:
    print("you are in a different family")


age = nameMichelle

if age < 13:
    print("You are a child")
elif age >=13 and age <=17:
    print("You are a teen")
else:
    print("You are an adult")




if "Amy" in family:
    print("Hello Amy")
else:
    print("no match")
