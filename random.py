import random

list = ["fire" , "water" , "space" , "heart" , "meat" , "plant"]
#print(list)
num = random.randint(0,5)
#print(num)
#print(list[num])

item = random.choice(list)
#print(item)

random.shuffle(list)
#print(list)

items = random.sample(list,num)
#print(items)
