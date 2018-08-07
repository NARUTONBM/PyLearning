def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total += v
    print("Total number of items: " + str(item_total))


def add_to_inventory(inventory, added_items):
    for i in range(len(added_items)):
        inventory.setdefault(added_items[i],0)
        inventory[added_items[i]] += 1

    return inventory


inv = {'rope': 1, 'gold coin': 42}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
