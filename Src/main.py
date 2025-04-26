from laibrary import Borrow

def menu():
    print('='*28)
    print()
    print("1. Add Book!")
    print("2. Borrow Book!")
    print('3. Return Book!')
    print('4. Exit')
    print('='*28)
    while True:
        choice_number=int(input('please enter your choice number: '))
        if choice_number == 1:
            print()
            data=Borrow()
            data.add_book()
            data.display_book()
            print()
        elif choice_number == 2:
            data=Borrow()
            data.brook_book()
            data.display_book()
        elif choice_number == 3:
            data=Borrow()
            data.return_book() 
                  
            data.display_book()
        elif choice_number == 4:
            break    
menu()


