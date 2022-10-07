def ContactBook():  # function to call other functions
    import ContactSource

    print("1. Display contact book\n2. Search for a contact\n3. Add a new contact\n4. Modify a contact\n5. Delete a contact\n6. Quit program\n")
    option = int(input("Enter a number: "))

    if option == 1:
        ContactSource.displayContact()
        print('\n\n–––––––––––––––––––––––––')  # divider between previous function and menu options
        ContactBook()  # call function again until user wants to quit
    elif option == 2:
        ContactSource.searchContact()
        print('\n–––––––––––––––––––––––––')
        ContactBook()
    elif option == 3:
        ContactSource.addContact()
        print('\n–––––––––––––––––––––––––')
        ContactBook()
    elif option == 4:
        ContactSource.modifyContact()
        print('\n–––––––––––––––––––––––––')
        ContactBook()
    elif option == 5:
        ContactSource.deleteContact()
        print('\n–––––––––––––––––––––––––')
        ContactBook()
    elif option == 6:
        quit()
    else:
        print("Please enter an integer from 1 to 5.")

ContactBook()