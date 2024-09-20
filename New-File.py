inventory = ["ham", "pepperoni", "sausage", "anchovies", "mushrooms", "bell peppers", "green onion"]
toppings = []
unavailable_toppings = ["pepperoni"]

EMPLOYEE_PASSWORD = "employee"  # Employee menu password

def display_customer_menu():
    print("""
    Customer Menu:
        1.) Add toppings to pizza
        2.) Remove toppings from pizza
        3.) Finish ordering
    """)

def display_employee_menu():
    print("""
    Employee Menu:
        1.) Add items to inventory
        2.) Remove items from inventory
        3.) Add items to unavailable_toppings (out-of-stock list)
        4.) Remove items from unavailable_toppings (out-of-stock list)
        5.) Exit Employee Menu
    """)

def customer_menu():
    while True:
        display_customer_menu()
        try:
            option = int(input("Choose an option: "))

            if option == 3:
                if toppings:
                    print("\nYour pizza has the following toppings:")
                    for top in toppings:
                        print(f"- {top}")
                else:
                    print("\nYou didn't add any toppings to your pizza.")
                print("Thank you for ordering!")
                break

            # Add toppings to pizza
            if option == 1:
                while True:
                    addtop = input("Add topping (or 'stop' to finish): ").lower()
                    if addtop == "stop":
                        break
                    if addtop not in inventory:
                        print(f"Sorry, {addtop} is not available in our inventory.")
                    elif addtop in unavailable_toppings:
                        print(f"Sorry, {addtop} is unavailable.")
                    elif addtop in toppings:
                        print(f"{addtop} is already added.")
                    else:
                        toppings.append(addtop)
                        print(f"{addtop} added to your pizza.")

            # Remove toppings from pizza
            elif option == 2:
                while True:
                    deltop = input("Remove topping (or 'stop' to finish): ").lower()
                    if deltop == "stop":
                        break
                    if deltop in toppings:
                        toppings.remove(deltop)
                        print(f"{deltop} removed from your pizza.")
                    else:
                        print(f"{deltop} is not on your pizza.")
            else:
                print("Invalid option. Please choose a number from 1 to 3.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")

def employee_menu():
    while True:
        display_employee_menu()
        try:
            option = int(input("Choose an option: "))

            if option == 5:
                break

            # Add items to inventory
            if option == 1:
                while True:
                    new_item = input("Add item to inventory (or 'stop' to finish): ").lower()
                    if new_item == "stop":
                        break
                    if new_item in inventory:
                        print(f"{new_item} is already in the inventory.")
                    else:
                        inventory.append(new_item)
                        print(f"{new_item} added to inventory.")

            # Remove items from inventory
            elif option == 2:
                while True:
                    remove_item = input("Remove item from inventory (or 'stop' to finish): ").lower()
                    if remove_item == "stop":
                        break
                    if remove_item in inventory:
                        inventory.remove(remove_item)
                        print(f"{remove_item} removed from inventory.")
                        # If the item is in unavailable_toppings, remove it from there as well
                        if remove_item in unavailable_toppings:
                            unavailable_toppings.remove(remove_item)
                            print(f"{remove_item} also removed from unavailable_toppings.")
                    else:
                        print(f"{remove_item} is not in the inventory.")

            # Add items to unavailable_toppings (out-of-stock list)
            elif option == 3:
                while True:
                    no_top_item = input("Add item to unavailable_toppings (out-of-stock) (or 'stop' to finish): ").lower()
                    if no_top_item == "stop":
                        break
                    if no_top_item in unavailable_toppings:
                        print(f"{no_top_item} is already in the unavailable_toppings list.")
                    elif no_top_item in inventory:
                        unavailable_toppings.append(no_top_item)
                        print(f"{no_top_item} added to unavailable_toppings list.")
                    else:
                        print(f"{no_top_item} is not in the inventory. Add it to the inventory first if you want to restrict it.")

            # Remove items from unavailable_toppings
            elif option == 4:
                while True:
                    remove_no_top = input("Remove item from unavailable_toppings (or 'stop' to finish): ").lower()
                    if remove_no_top == "stop":
                        break
                    if remove_no_top in unavailable_toppings:
                        unavailable_toppings.remove(remove_no_top)
                        print(f"{remove_no_top} removed from unavailable_toppings list.")
                    else:
                        print(f"{remove_no_top} is not in the unavailable_toppings list.")

            else:
                print("Invalid option. Please choose a number from 1 to 5.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Inventory: {inventory}")
    print(f"Unavailable toppings: {unavailable_toppings}")

def access_employee_menu():
    password = input("Enter employee password: ")
    if password == EMPLOYEE_PASSWORD:
        employee_menu()
    else:
        print("Incorrect password. Access denied.")

# Main program loop to switch between customer and employee menu
while True:
    print("""
    Welcome! Please select:
        1.) Customer Menu (Order Pizza)
        2.) Employee Menu (Manage Inventory)
        3.) Exit Program
    """)
    
    try:
        main_option = int(input("Choose an option: "))

        if main_option == 1:
            customer_menu()

        elif main_option == 2:
            access_employee_menu()

        elif main_option == 3:
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 3.")
    
    except ValueError:
        print("Invalid input. Please enter a number.")
