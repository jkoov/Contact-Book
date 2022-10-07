contactsFirst=[]  # list that contains all contacts' first names
contactsLast=[]  # list that contains all contacts' last names
contactsPhone=[]  # list that contains all contacts' phone numbers
contactsEmail=[]  # list that contains all contacts' email addresses
contactsBirthday=[]  # list that contains all contacts' birthday
contactsNote=[]  # list that contains all contacts' notes


def displayContact():  # display entire contact book
    print("\n–––DISPLAY CONTACT BOOK---\n")

    print("{: <20} {: <20} {: <20} {: <40} {: <20} {: <20}".format('FIRST NAME', 'LAST NAME', 'PHONE #', 'EMAIL',
                                                                   'BIRTHDAY', 'NOTE'))  # contact book header
    print('–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––')
    for i in range(0, len(contactsFirst)):  # print all contacts neatly
        print("{: <20} {: <20} {: <20} {: <40} {: <20} {: <20}".format(contactsFirst[i], contactsLast[i], contactsPhone[i],
                                                                  contactsEmail[i], contactsBirthday[i], contactsNote[i]))


def searchContact():  # search for contact in contact book
    print("\n---SEARCH FOR A CONTACT---\n")
    print("a. By first name\nb. By last name\nc. By phone number\nd. By email address\ne. By birthday\n")  # provide ways to search for contact

    search = input("Enter search option: ")
    search = search.strip().lower()

    if search == 'a':  # search contact by first name
        find = input("Enter contact's first name: ")
        find = find.strip().capitalize()

        if find in contactsFirst:  # check if entered first name in first name list
            i = int(contactsFirst.index(find))  # obtain index of input in first name list
            print("\nName:", contactsFirst[i], contactsLast[i], "\nPhone:", contactsPhone[i], "\nEmail:",
                  contactsEmail[i], "\nBirthday:", contactsBirthday[i], "\nNote:", contactsNote[i])
        else:
            print("\nA contact with the first name " + "\"" + find + "\"", "cannot be found.\n")

    elif search == 'b':  # search contact by last name
        find = input("Enter contact's last name: ")
        find = find.strip().capitalize()

        if find in contactsLast:  # check if entered last name in last name list
            i = int(contactsLast.index(find))  # obtain index of input in last name list
            print("\nName:", contactsFirst[i], contactsLast[i], "\nPhone:", contactsPhone[i], "\nEmail:",
                  contactsEmail[i], "\nBirthday:", contactsBirthday[i], "\nNote:", contactsNote[i])
        else:
            print("\nA contact with the last name " + "\"" + find + "\"", "cannot be found.\n")

    elif search == 'c':  # search contact by phone number
        find = input("Enter contact's phone number: ")
        find = find.strip()

        if find in contactsPhone:  # check if entered phone number in phone number list
            i = int(contactsPhone.index(find))  # obtain index of input in phone number list
            print("\nName:", contactsFirst[i], contactsLast[i], "\nPhone:", contactsPhone[i], "\nEmail:",
                  contactsEmail[i], "\nBirthday:", contactsBirthday[i], "\nNote:", contactsNote[i])
        else:
            print("\nA contact with the phone number " + "\"" + find + "\"", "cannot be found.\n")

    elif search == 'd':  # search contact by email
        find = input("Enter contact's email address: ")
        find = find.strip()

        if find in contactsEmail:  # check if entered email in email list
            i = int(contactsEmail.index(find))  # obtain index of input in email list
            print("\nName:", contactsFirst[i], contactsLast[i], "\nPhone:", contactsPhone[i], "\nEmail:",
                  contactsEmail[i], "\nBirthday:", contactsBirthday[i], "\nNote:", contactsNote[i])
        else:
            print("\nA contact with the email address " + "\"" + find + "\"", "cannot be found.\n")

    elif search == 'e':  # search contact by birthday
        find = input("Enter contact's birthday (MM/DD/YYYY): ")
        find = find.strip()

        if find in contactsBirthday:  # check if entered birthday in birthday list
            i = int(contactsBirthday.index(find))  # obtain index of input in birthday list
            print("\nName:", contactsFirst[i], contactsLast[i], "\nPhone:", contactsPhone[i], "\nEmail:",
                  contactsEmail[i], "\nBirthday:", contactsBirthday[i], "\nNote:", contactsNote[i])
        else:
            print("\nA contact with the birthday " + "\"" + find + "\"", "cannot be found.\n")


def addContact():  # add new contact to contact book
    print("\n---ADD A NEW CONTACT---\n")
    print("Enter the details of a new contact below.\nYou must enter the contact's first name, last name, and phone"
          " number and/or email address.\nIf you do not want to include a specific detail, click enter.")  # instructions
    first = input("\nEnter first name: ")
    last = input("Enter last name: ")

    import sys
    for i in range(sys.maxsize**100):  # repeatedly ask user for both first & last name until entered
        if first == '':
            print("\nError. You must enter the contact's first name.")
            first = input("Enter first name: ")

        elif last == '':
            print("\nError. You must enter the contact's last name.")
            last = input("Enter last name: ")

        elif first != '' and last != '':
            break

    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    for i in range(sys.maxsize**100):  # repeatedly ask user for either phone or email until entered
        if phone == '' and email == '':
            print("\nError. You must enter the contact's phone number and/or email address.")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")

        elif (phone != '' or email != '') or (phone != '' and email != ''):
            break

    birthday = input("Enter birthday (MM/DD/YYYY): ")
    note = input("Enter note: ")

    # remove whitespace from inputs
    # capitalize first & last name
    first = first.strip().capitalize()
    last = last.strip().capitalize()
    phone = phone.strip()
    email = email.strip()
    birthday = birthday.strip()
    note = note.strip()

    # append new contact's details to corresponding lists
    contactsFirst.append(first)
    contactsLast.append(last)
    contactsPhone.append(phone)
    contactsEmail.append(email)
    contactsBirthday.append(birthday)
    contactsNote.append(note)

    # display new contact's information
    print("\nName:", first, last, "\nPhone:", phone, "\nEmail:", email, "\nBirthday:", birthday, "\nNote:", note)


def modifyContact():  # modify already existing contact
    print("\n---MODIFY A CONTACT---\n")
    firstAndLast = input("Enter first and last name of contact you want to modify: ")
    firstAndLast = firstAndLast.title().split(' ')

    first = firstAndLast[0]
    last = firstAndLast[1]

    print("\na. First Name\nb. Last Name\nc. Phone Number\nd. Email Address\ne. Birthday\nf. Note\n")  # options for which detail to modify
    modify = input("What detail would you like to change? ")
    modify = modify.lower()

    if (first in contactsFirst) and (last in contactsLast):  # check first & last name in corresponding lists
        # find index of input in first name list
        # since contact exists in book, index can be used for all options
        i = int(contactsFirst.index(first))

        if modify == 'a':
            new = input("Enter the new first name: ")
            contactsFirst[i] = new.strip().capitalize()  # update specific element in first name list according to index

            print("\nName:", contactsFirst[i], contactsLast[i], "\nPhone:",
                  contactsPhone[i], "\nEmail:", contactsEmail[i], "\nBirthday:", contactsBirthday[i], "\nNote:", contactsNote[i])

        elif modify == 'b':
            new = input("Enter new last name: ")
            contactsLast[i] = new.strip().capitalize()  # update specific element in last name list according to index

            print("\nName:", contactsFirst[i], contactsLast[i], "\nPhone:",
                  contactsPhone[i], "\nEmail:", contactsEmail[i], "\nBirthday:", contactsBirthday[i], "\nNote:", contactsNote[i])

        elif modify == 'c':
            new = input("Enter new phone number: ")  #
            contactsPhone[i] = new.strip()  # update specific element in phone list according to index

            print("\nName:", contactsFirst[i], contactsLast[i], "\nPhone:",
                  contactsPhone[i], "\nEmail:", contactsEmail[i], "\nBirthday:", contactsBirthday[i], "\nNote:", contactsNote[i])

        elif modify == 'd':
            new = input("Enter new email address: ")
            contactsEmail[i] = new.strip()  # update specific element in email list according to index

            print("\nName:", contactsFirst[i], contactsLast[i], "\nPhone:",
                  contactsPhone[i], "\nEmail:", contactsEmail[i], "\nBirthday:", contactsBirthday[i], "\nNote:", contactsNote[i])

        elif modify == 'e':
            new = input("Enter new birthday: ")
            contactsBirthday[i] = new.strip()  # update specific element in birthday list according to index

            print("\nName:", contactsFirst[i], contactsLast[i], "\nPhone:",
                  contactsPhone[i], "\nEmail:", contactsEmail[i], "\nBirthday:", contactsBirthday[i], "\nNote:", contactsNote[i])

        elif modify == 'f':
            new = input("Enter new note: ")
            contactsNote[i] = new.strip()  # update specific element in note list according to index

            print("\nName:", contactsFirst[i], contactsLast[i], "\nPhone:",
                  contactsPhone[i], "\nEmail:", contactsEmail[i], "\nBirthday:", contactsBirthday[i], "\nNote:", contactsNote[i])

    else:
        print("\nA contact with the name " + "\""+' '.join(firstAndLast)+"\"", "cannot be found.")


def deleteContact():  # delete already existing contact
    print("\n---DELETE A CONTACT---\n")
    firstAndLast = input("Enter first and last name of contact you want to delete: ")
    firstAndLast = firstAndLast.title().split(' ')

    first = firstAndLast[0]
    last = firstAndLast[1]

    first = first.strip().capitalize()
    last = last.strip().capitalize()

    if (first in contactsFirst) and (last in contactsLast):  # check if contact exists
        i = int(contactsFirst.index(first))
        k = int(contactsLast.index(last))

        if i == k:  # check that indexes match
            print("\nName:", contactsFirst[i], contactsLast[i], "\nPhone:", contactsPhone[i], "\nEmail:", contactsEmail[i],
                  "\nBirthday:", contactsBirthday[i], "\nNote:", contactsNote[i], "\n")  # show contact to double check
            delete = input("Do you want to delete this contact?\nEnter \"Yes\" or \"No\": ")
            delete = delete.strip().capitalize()

            if delete == 'Yes':  # remove contact's details from all lists
                contactsFirst.pop(i)
                contactsLast.pop(i)
                contactsPhone.pop(i)
                contactsEmail.pop(i)
                contactsBirthday.pop(i)
                contactsNote.pop(i)

                print("\nThis contact has been deleted.")

            elif delete == 'No':
                print("\nThis contact has NOT been deleted.")

    else:
        print("\nA contact with the name " + "\""+' '.join(firstAndLast)+"\"", "cannot be found.")