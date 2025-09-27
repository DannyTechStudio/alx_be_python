

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
    
def main():
    shopping_list = []
    
    while True:
        display_menu()

        choice = input("Choose option 1-4: ")

        if choice == '1':
            item = input("Enter item name: ")
            shopping_list.append(item)
        elif choice == '2':
            item = input("Enter item name to be removed: ")
            if shopping_list.__contains__():
                shopping_list.remove()
            else:
                print(f"{item} is not in your list.")
        elif choice == '3':
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  