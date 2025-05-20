# Contact-Book

# Contact
A simple Python-based contact book application that allows users to store, view, search, and delete contacts with proper input validation.

***Features***

  1. Contact Management:
      - Add new contacts with name and phone number
      - View all saved contacts
      - Search for specific contacts
      - Delete existing contacts
  2. Input Validation:
      - Name cannot be empty or numeric
      - Phone number must be 1-10 digits and numeric
      - Prevents duplicate contacts
      - Validates menu choices
  3. User-Friendly Interface:
      - Clear menu system
      - Numbered contact display
      - Helpful error messages
      - Clean exit option

***How to Use***

  1. Running the Application:
      - Save the code as ```contact_book.py```
      - Run with Python: ```python contact_book.py```

  2. Menu Options:
     
      ```
      1. Add Contact
      2. All Contacts
      3. Search Contact
      4. Delete Contact
      5. Exit
      ```
  3. Adding a Contact:
      - Enter a non-empty name (cannot be numbers)
      - Enter a 1-10 digit phone number
      - Application validates both inputs before saving

  4. Viewing Contacts:
      - Displays all contacts in numbered list
      - Shows "No contacts found" if empty
  5. Searching Contacts:
      - Search by exact name match
      - Returns phone number or "Not Found"

  6. Deleting Contacts:
      - Delete by exact name match
      - Confirms deletion or "Contact not found"

  7. Exiting:
      - Gracefully exits the application

***Example Usage***
```
Welcome to Contact Book
1. Add Contact
2. All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter a no:1
Enter a Name: John Doe
Enter a Phone Number (1-10 digits): 1234567890
Contact added successfully!

1. Add Contact
2. All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter a no:2

All Contacts:
1. John Doe: 1234567890

1. Add Contact
2. All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter a no:5
Good Bye!
Exiting contact book...
```
***Error Handling***

The application handles:

  - Empty inputs
  - Numeric names
  -Non-numeric phone numbers
  - Phone numbers that are too short/long
  - Duplicate contacts
  - Invalid menu choices
  - Search/delete of non-existent contacts
