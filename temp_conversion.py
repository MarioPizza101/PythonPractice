temp1 = 50
temp2 = "FK"

def convert(temp1,temp2):
    if temp2 == "FC":
        value = (temp1 - 32) * 5/9
        print(f"{value} degrees celsius")
    elif temp2 == "FK":
        value = (temp1 - 32) * 5/9 + 273.15
        print(f"{value} degrees kelvin")
    elif temp2 == "CF":
        value = (temp1 * 9/5) + 32
        print(f"{value} degrees farenheit")
    elif temp2 == "CK":
        value = temp1 + 273.15
        print(f"{value} degrees kelvin")
    elif temp2 == "KF":
        value = (temp1 - 273.15) * 9/5 + 32
        print(f"{value} degrees farenheit")
    elif temp2 == "KC":
        value = temp1 - 273.15
        print(f"{value} degrees celsius")
    else:
        pass

convert(temp1,temp2)
