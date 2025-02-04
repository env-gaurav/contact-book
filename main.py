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
    print("success")

def main():
    contacts={}
    display_msg()
    while True:
        choice=int(input("Enter Choice: "))
        if choice == 6:
            print(contacts)
            print("Exit")
            break
        elif choice == 1:
            add_contact(contacts)
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()