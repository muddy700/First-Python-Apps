print("\n CONTACT BOOK")

def menu():
    print("\nChoose Menu")
    print(" 1. View Contacts")
    print(" 2. Add Contact")
    print(" 3. Delete Contact")
    print(" 4. Edit Contact")
    print(" 5. Search Contact")
    print(" 6. Close Book")
    selectedMenu = input(" : > ")
    operations(selectedMenu)
    
def repeatMenu():
    option = input("\nPress 1, To Continue Or Anything To Exit : > ")   
    if option == '1':
        menu()
    else:
        exit()

def operations(operation):
    if not operation.isdigit():
        print("Enter Valid Menu")
        menu()
    elif  operation == '1':
        showContacts()
        repeatMenu()
    elif  operation == '2':
        addContact()
        repeatMenu()
    elif  operation == '3':
        deleteContact()
        repeatMenu()
    elif  operation == '4':
        editContact()
        repeatMenu()
    elif  operation == '5':
        searchContact()
        repeatMenu()
    elif operation == '6':
        print("\n See You Next Time Buddy!")
        exit()
    else:
        print("Menu Not Found")
        menu()
class Contact:
    def __init__(self, phone, name):
        self.phone = phone
        self.name = name

searchedList = []
contactsList = []
contactsList.append(Contact(123, 'Cathy'))
contactsList.append(Contact(311, 'Asma'))
contactsList.append(Contact(331, 'Chiddy'))
contactsList.append(Contact(122, 'Mwaisa'))
contactsList.append(Contact(432, 'Nyonyoma'))

def showContacts():
    print("\n   Contacts List")
    print(" Id \t Phone \t Name")
    for x in range(len(contactsList)):
        print('', x+1, '\t', contactsList[x].phone, '\t', contactsList[x].name)

def addContact():
    Number = input("Number : > ")
    Name = input("Name : > ")
    contactsList.append(Contact(Number, Name))
    print(Name, "Added Successful")

def deleteContact():
    contactId = input("Enter Contact Id : > ")
    if not contactId.isdigit():
        print("Invalid Id")
        repeatMenu()
    elif not int(contactId)-1 in range(len(contactsList)):
        print("Id Not Found")
        repeatMenu()
    for x in range(len(contactsList)):
        if x == int(contactId)-1:
            print(contactsList[x].name, "Deleted Successful.")
            contactsList.pop(x)

def editContact():
    contactId = input("Enter Contact Id : > ")

    if not contactId.isdigit():
        print("Invalid Id")
        repeatMenu()
    elif not int(contactId)-1 in range(len(contactsList)):
        print("Id Not Found")
        repeatMenu()

    print("\nBefore\n")
    print(" Id \t Phone \t Name")
    for x in range(len(contactsList)):
        if x == contactId-1:
            print('', contactId, '\t', contactsList[x].phone, '\t', contactsList[x].name)
            newPhone = input("\nNew Phone : > ")
            newName = input("New Name : > ")
            contactsList[x].phone = newPhone
            contactsList[x].name = newName
            print("\nContact Edited Successful.")
            print("\nAfter\n")
            print(" Id \t Phone \t Name")
            print('', contactId, '\t', contactsList[x].phone, '\t', contactsList[x].name)

def searchContact():
    letter = input("Type letter To Search : > ")
    for x in range(len(contactsList)):
        if letter in contactsList[x].name:
            searchedList.append(contactsList[x])
    if len(searchedList) > 0:
        print("\n   Search Results")
        print(" Id \t Phone \t Name")
        for x in range(len(searchedList)):
            print('', x+1, '\t', searchedList[x].phone, '\t', searchedList[x].name)

    else:
        print("No Items Match Your Search")
    searchedList.clear()

menu()