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
    
def main():
    contact={}
    display_msg()
    while True:
        choice=int(input("Enter Choice: "))
        if choice == 6:
            print("Exit")
            break
        elif choice == 1:
            pass
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