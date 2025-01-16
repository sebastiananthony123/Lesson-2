shopping_list = []

while True:
    print("\nShopping List Menu:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3.Show List")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"Added: '{item}'")
    elif choice == '2':
        item_to_remove = input("Enter the item to remove: ")
        if item_to_remove in shopping_list:
            shopping_list.remove(item_to_remove)
            print(f"Removed: '{item_to_remove}'")
        else:
            print("Item not found in the list.")
    elif choice == '3':
        print("Your shopping list:")
        for index, item in enumerate(shopping_list):
            print(f"{index + 1}. {item}")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid option, please try again.")


