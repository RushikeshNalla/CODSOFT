
# To-Do List application

def display_menu():
    print("\nTo-Do List Menu")
    print("1. View To-Do List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Exit")

def view_list(todo_list):
    print("\nTo-Do List:")
    if len(todo_list) == 0:
        print("No items in the list.")
    else:
        for idx, item in enumerate(todo_list, start=1):
            print(f"{idx}. {item}")

def add_item(todo_list):
    item = input("Enter the item to add: ")
    todo_list.append(item)
    print(f"'{item}' has been added to the list.")

def remove_item(todo_list):
    view_list(todo_list)
    try:
        item_num = int(input("Enter the number of the item to remove: "))
        if 1 <= item_num <= len(todo_list):
            removed_item = todo_list.pop(item_num - 1)
            print(f"'{removed_item}' has been removed from the list.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            view_list(todo_list)
        elif choice == '2':
            add_item(todo_list)
        elif choice == '3':
            remove_item(todo_list)
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()