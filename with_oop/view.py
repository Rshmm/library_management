from manage_library import PersonManagement,BookManagement,Borrow

person_manager = PersonManagement()
book_manager = BookManagement()
borrow_manager= Borrow(person_manager,book_manager)

while True:

    while True:
        print("*" * 50)
        print("1-add book \n2-show books \n3-remove book \n4-edit book \n5-add person "
              "\n6-show persons \n7-remove person \n8-edit person \n9-borrow book \n10-show borrows "
              "\n0-exit ")
        print("*" * 50)

        choice = int(input("Enter your choice : "))

        print("*" * 50)

        match choice:
            # add book
            case 1:
                code = input("Enter book code : ")
                name = input("Enter book name : ")
                book_manager.add_book(code,name)
            # show books
            case 2:
               book_manager.show_book()
            # remove book
            case 3:
                book_manager.show_book()
                code = input("Enter book code which you wants to remove : ")
                book_manager.remove_book(code)

            # edit book
            case 4:
                book_manager.show_book()
                code = input("enter book code which you wants to edit : ")
                new_name = input("Enter book new name : ")
                book_manager.edit_book(code,new_name)

            # add person
            case 5:
                code = input("Enter person code : ")
                name = input("Enter person name : ")
                family = input("Enter person family name : ")
                person_manager.add_person(code,name,family)

            # show persons
            case 6:
                person_manager.show_person()

            # remove person
            case 7:
               person_manager.show_person()
               code = input("Enter person code that you wats to remove : ")
               person_manager.remove_person(code)

            # edit person
            case 8:
                person_manager.show_person()
                code = input("Enter person code that you wants to edit : ")
                new_name = input("Enter person new name : ")
                new_family = input("Enter person new family name : ")
                person_manager.edit_person(code,new_name,new_family)

            # barrow book
            case 9:
                person_manager.show_person()
                person_code = input("Enter person code : ")
                book_manager.show_book()
                book_code = input("Enter book code : ")
                borrow_manager.borrow_book(person_code,book_code)

            # show barrows
            case 10:
                borrow_manager.show_borrows()

            case 0:
                exit()