#Eugen Mboya
#BSCIT-05-0003/2024

# Initialize empty inventory
inventory = {}

while True:
    print("\nInventory Menu")
    print("1. Add or update an item")
    print("2. Retrieve item information")
    print("3. Display total quantity of all items")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))

        if item_name in inventory:
            inventory[item_name] += quantity
            print(f"Updated {item_name}. New quantity: {inventory[item_name]}")
        else:
            inventory[item_name] = quantity
            print(f"Added {item_name} with quantity {quantity}")

    elif choice == "2":
        item_name = input("Enter item name to retrieve: ")

        if item_name in inventory:
            print(f"{item_name} quantity: {inventory[item_name]}")
        else:
            print("Item not found in inventory.")

    elif choice == "3":
        total_quantity = sum(inventory.values())
        print("Total quantity of all items:", total_quantity)

    elif choice == "4":
        print("Exiting inventory system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
