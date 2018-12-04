# Hero's Inventory | Jack Pike | 2018

import os
import random

player_health = 100
player_armor = 1250
player_attack = 250
player_money = 0
def prompt():
    input("\nPress the enter key to continue: ")

def clear_screen():
    os.system('cls')


def hud():
    print("Stats: ", player_stats)
    print("Inventory: ", inventory)
    print("Equipped: ", equipped)


chest_items = ["Gold", "Gems", "Elven Sword", "Bow", "Crossbow", "Boots", "Hat", "Traps"]
inventory = [
    "Rusty Sword", "Leather Armor", "Wood Shield", "lvl 1 Healing Potion"
]
max_inventory = 10
equipped = []
player_stats = ["Health", player_health, "Armor", player_armor, "Attack", player_attack, "Money", player_money]

print("As you set out on your journey, you have the following: ")
print("Player Stats: ")
print(player_stats)
print()
print("Your items include: ")
for item in inventory:
    print(item)

input("Press enter to continue: ")
os.system('cls')
hud()

print("You have", len(inventory), "/", max_inventory, "items in your possession.")
print("You can pick up", max_inventory - len(inventory), "more items. ")
prompt()
os.system('cls')
hud()

print("You were attacked!")
player_stats[1] -= 22
input("Press the enter key to continue: ")
clear_screen()
hud()

input("\nYou have taken some damage on your journey \n" +
      "Your health is at: " + str(player_stats[1]) + "\n" +
      "You need to use your healing potion \nPress the enter key to continue.")

if "lvl 1 Healing Potion" in inventory:
    clear_screen()
    hud()
    print("You will live to fight another day, you owe your life to the 'Lvl 1 Healing Potion'")
    player_stats[1] += 20
    inventory.remove("lvl 1 Healing Potion")
input("\nPress the enter key to continue: ")
clear_screen()
hud()

for i in range(len(inventory)):
    print(str(i), inventory[i])
print("Lets quip some armor: ")
index = int(input("\nEnter the index number for an armor item in your inventory you wish to equip: "))

while index > len(inventory)-1 or index < 0 and index != "":
    print("That number is out of range")
    index = int(input("\nEnter the index number for an armor item in your inventory you wish to equip: "))
print("You equip your ", inventory[index])
equipped.append(inventory[index])
inventory.remove(inventory[index])
if "Leather Armor" in equipped:
    player_stats[3] += 1000
if "Wood Shield" in equipped:
    player_stats[3] += 500
clear_screen()
hud()

chest = []
for i in range(random.randrange(len(chest_items))):
    item = random.choice(chest_items)
    chest.append(item)

print("You find a chest which contains: ")
print(chest)
print()
print("You add the contents of the chest to your inventory.")
if len(inventory) + len(chest) < max_inventory:
    inventory += chest
else:
    print("You don't have enough room in your inventory!")
    drop = len(inventory) + len(chest) - max_inventory
    for i in range(drop):
        x = random.choice(chest)
        chest.remove(x)
    inventory += chest
hud()


print("Convert treasure to gold")
if "Gold" in inventory:
    player_stats[7] += 100
    inventory.remove("Gold")
if "Gems" in inventory:
    player_stats[7] += 1000
    inventory.remove("Gems")
prompt()
clear_screen()
hud()

if player_stats[7] > 100:
    print("You want to trade your sword for a crossbow. You sell your \n"+
          " sword for 20 gold and buy a crossbow for 100 gold")
    player_stats[7] += 20
    player_stats[7] -= 100
    inventory[0] = "Crossbow"
prompt()
clear_screen()
hud()

print("You trade in the last 2 items from your inventory for a new item. ")
inventory[len(inventory)-2:len(inventory)] = ["Orb of future telling"]
prompt()
clear_screen()
hud()
if "Wood Shield" in inventory:
    print("In a great battle, your shield is destroyed.")
    for i in range(len(inventory)):
        if inventory[i] == "Wood Shield":
            del inventory[i]
    for i in range(len(equipped)):
        if equipped[i] == "Wood Shield":
            del equipped[i]

prompt()
clear_screen()
hud()
