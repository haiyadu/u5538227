inventory = {}

def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"Added {quantity} {item}(s).")

def view_inventory():
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def update_item(item, quantity):
    if item in inventory:
        inventory[item] = quantity
        print(f"Updated {item} quantity to {quantity}.")
    else:
        print(f"{item} not found in inventory.")
        
def check_item(item):
    if item in inventory:
        print(f"{item}have{inventory[item]}")
    else:
        print(f"{item}disappear")
        

def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Check Item Quantity")
        print("5. Exit")
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(item, quantity)
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            item = input("Enter item name: ")
            quantity = int(input("Enter new quantity: "))
            update_item(item, quantity)
        elif choice == '4':
            item = input("Enter item name: ")
            check_item(item)
        elif choice == '5':
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid choice. Please choose again.")

manage_inventory()
