contacts={}

while True:
    print("Welcome a Contact Book\n1.Add Contact\n2.All Contacts\n3.Search Contact\n4.Delete Contact\n5.Exit")
    choice=(input("Enter a no:"))
    if choice=="1":
        # Name Validation
        while True:
            name=input("Enter a Name:").strip()
            if not name:  # Check for empty input
                print("Error: Name cannot be empty. Please try again.")
            elif name.isdigit():
                print("Error: Name cannot be a number. Please try again.")
            elif name in contacts:  # Check if name already exists
                print("Error: Contact already exists. Please try again.")
            else:
                break
        # Number validation
        while True:
            phone = input("Enter a Phone Number (1-10 digits): ").strip()
            if not phone:
                print("Error: Phone number cannot be empty. Please try again.")
            elif not phone.isdigit():
                print("Error: Phone number must contain only numbers. Please try again.")
            elif len(phone) < 1 or len(phone) > 10:  # Check length range
                print("Error: Phone number must be 1 to 10 digits long. Please try again.")
            elif phone in contacts:  # Check if name already exists
                print("Error: Contact already exists. Please try again.")
            else:
                contacts[name] = phone
                print("Contact added successfully!")
                break
    elif choice=="2":
        if not contacts:
            print("\nNo contacts found!")
        else:
            print("\nAll Contacts:")
            for i, (name, phone) in enumerate(contacts.items(), 1):
                print(f"{i}. {name}: {phone}")
    elif choice=="3":
        search=input("Enter name search:").strip()
        if search in contacts:
            print(f"{search}:{contacts[search]}")
        else:
            print("Not Found")  
    elif choice=="4":
        delete=input("Enter name to delete: ")
        if delete in contacts:
            del contacts[delete]
            print("Contact deleted!")
        else:
            print("Contact not found!")
    elif choice=="5":
        print("Good Bye!\nExiting contact book...")
        break
    else:
        print("Invalid choice! Please enter a number between 1-5.")