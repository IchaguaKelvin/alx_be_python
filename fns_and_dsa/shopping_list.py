# Initialize the shopping list
shopping_list = []

def display_menu():
    """Displays the main menu options."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item():
    """Prompts the user for an item and adds it to the list."""
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"'{item}' has been added to the list.")

def remove_item():
    """Prompts the user for an item and removes it from the list if found."""
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the list.")
    else:
        print(f"'{item}' is not in the list.")

def view_list():
    """Displays the current items in the shopping list."""
    if shopping_list:
        print("\n--- Current Shopping List ---")
        for index, item in enumerate(shopping_list, 1):
            print(f"{index}. {item}")
        print("---------------------------")
    else:
        print("The shopping list is empty.")

def main():
    """Main function to run the shopping list manager loop."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            view_list()
        elif choice == '4':
            print("Exiting Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()