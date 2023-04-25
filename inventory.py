Name = "Steve"
Health = 5
Magic = 10
Damage = 1*4

Locations = ["desert" , "ocean" , "grassland" , "castle"]
Enemy_Drops = ["hearts" , "xp" , "bark" , "silver"]
Location_Grassland = ["crystal" , "bomb" , "hearts" , "stone" , "silver" ,"bark"]

Inventory = ["bomb" , "metal" , "silver" , "crystal"]
print(Inventory)

if ("metal" in Inventory) and ("silver" in Inventory):
    Inventory.remove("metal")
    Inventory.remove("silver")
    Inventory.append("sword")
    print("You crafted a sword")
else:
    print("You don't have the correct items.")

if ("crystal" in Inventory) and ("bark" in Inventory):
    Inventory.remove("crystal")
    Inventory.remove("bark")
    Inventory.append("wand")
    print("You crafted a wand")
else:
    print("You don't have the correct items.")
print(Inventory)
