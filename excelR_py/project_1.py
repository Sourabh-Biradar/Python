# project 1
# simple contact list 

contacts={}   # {name:number}

def add_to_contacts():
    name = input("Enter name :").strip()
    number = input("Enter phone number :").strip()

    if name in contacts and contacts[name] == number:
        print("Contact already exsists!")
    else:
        if len(number)==10:
            contacts[name] = number
            print("Contact added successfully")
        else:
            print("Enter valid number")
        print(contacts)

def search_contact():
    name = input("Enter name :").strip()
    if name in contacts:
        print(f'{name} : {contacts[name]}')
    else :
        print("No contact found")

def show_contacts():
    print(contacts)

def delete_contact():
    name = input("Enter name :").strip()
    if name in contacts:
        contacts.pop(name)
        print("Contact deleted successfully")
    else :
        print("No contact found")

while True:
    print("1.Add contact")
    print("2.Search contact")
    print("3.Show all contacts")
    print("4.Delete contact")
    print("5.Exit program")

    i = input("Enter option :")

    if i=='1':
        add_to_contacts()
    elif i=='2':
        search_contact()
    elif i=='3':
        show_contacts()
    elif i=='4':
        delete_contact()
    elif i=='5':
        break
    else:
        print("Enter valid option")
