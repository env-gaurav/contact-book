def display_msg():
    msg='''
     CONTACT BOOK
     ------------
    1. Add Contact
    2. Search Contact
    3. Update Contact
    4. Delete Contact
    5. Display Contact
    6. Exit 
'''
    return print(msg)

def add_contact(contacts):
    name=input("Enter Name: ")
    phone=input("Enter Phone: ")
    email=input("Enter Email: ")
    address=input("Enter Address: ")
    contacts[name]={"Phone":phone, "Email":email, "Address":address}
    print("Record added successfully")

def display_contacts(contacts):
    print(contacts)

def update_contact(contacts):
    name= input("Enter Name: ")
    phone=input("Enter Phone: ")
    email=input("Enter Email: ")
    address=input("Enter Address: ")
    contacts[name]={"Phone":phone, "Email":email, "Address":address}
    print("Record updated successfully")

def search_contact(contacts):
    name= input("Enter Name: ")
    contact = contacts.get(name,"Not found")
    print(contact)

def delete_contact(contacts):
    name= input("Enter name to delete: ")
    if name in contacts:
        contacts.pop(name)
        print("Record deleted successfully")

def main():
    contacts={
        'Alice': {'phone': '123-456-7890', 'email': 'alice@example.com', 'address': '123 Maple Street'},
    'Bob': {'phone': '987-654-3210', 'email': 'bob@example.com', 'address': '456 Oak Avenue'},
    'Charlie': {'phone': '555-555-5555', 'email': 'charlie@example.com', 'address': '789 Pine Road'}
    }
    display_msg()
    while True:
        choice=int(input("Enter Choice: "))
        if choice == 6:
            print("Exit")
            break
        elif choice == 1:
            add_contact(contacts)
        elif choice == 2:
            search_contact(contacts)
        elif choice == 3:
            update_contact(contacts)
        elif choice == 4:
            delete_contact(contacts)
        elif choice == 5:
            display_contacts(contacts)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()