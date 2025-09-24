

def display_menu():
    # Display the shopping list menu.
    print("\n----Shopping List Manager----")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List of Items")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("\nChoose an option (1-4): ").strip()
        if choice == "1":
            item = input("\nEnter an item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'\n{item}' has been added to the shopping list.")
            else:
                print("Item cannot be empty.")
        elif choice == "2":
            item = input("\nEnter an item to remove: ").strip()
            if item:
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f'"{item}" removed from the shopping list successfully.')
                else:
                    print(f'Item "{item}" not found in the shopping list.')
            else:
                print("Item cannot be empty.")
        elif choice == "3":
            if shopping_list:
                print("\n=====Current Shopping List of Items======")
                for index, item in enumerate(shopping_list):
                    print(f"{index + 1}. {item}")
            else:
                print("The shopping list is currently empty.")
        elif choice == "4":
            print("\nExiting the Shopping List Manager...")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()