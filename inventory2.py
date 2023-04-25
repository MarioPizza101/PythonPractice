Inventory = ["hydro" , "oxygen" , "plants" , "metal"]
action = "crafting"
item = "water"

def crafting(item):
    if item =="water":
        if ("hydro" in Inventory) and ("oxygen" in Inventory):
            Inventory.remove("hydro")
            Inventory.remove("oxygen")
            Inventory.append("water")
            print("YOU CRAFTED WATER")
        else:
            print("YOU DONT HAVE THE CORRECT ITEMS")
    elif item == "sword":
        pass
    elif item == "cake":
        pass

if action== "crafting":
    crafting(item)
elif action == "attack":
    attack()
else:
    print("nothing happens")
