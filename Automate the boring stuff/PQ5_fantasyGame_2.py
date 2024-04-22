stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for key, value in inventory.items():
        print(str(value) + " " + key)
        item_total = item_total + int(value)
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory[i] = inventory.get(i,0)+1
        
    return inventory

displayInventory(stuff)
stuff = addToInventory(stuff, dragonLoot)
print()
displayInventory(stuff)
