from module import *

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
            add_book(code, name)

        # show books
        case 2:
            show_books()

        # remove book
        case 3:
            show_books()
            code = input("Enter book code that you wants to remove :  ")
            remove_book(code)

        # edit book
        case 4:
            show_books()
            code = input("Enter book code that you wants to edit ")
            new_name = input("Enter person new name : ")
            edit_book(code, new_name)

        # add person
        case 5:
            code = input("Enter person code : ")
            name = input("Enter person name : ")
            family = input("Enter person family name : ")
            add_person(code, name, family)

        # show persons
        case 6:
            show_persons()

        # remove person
        case 7:
            show_persons()
            code = input("Enter person code that you wants to remove :  ")
            remove_person(code)

        # edit person
        case 8:
            show_persons()
            code = input("Enter person code that you wants to edit :  ")
            new_name = input("Enter person new name  :  ")
            new_family = input("Enter person new family name  :  ")
            edit_person(code, new_name, new_family)

        # barrow book
        case 9 :
            show_persons()
            code_person = input("Enter person code who wants to borrow : ")
            show_books()
            code_book = input("Enter book code which person wants to borrow : ")
            borrow_book(code_person, code_book)

        # show barrows
        case 10:
           show_borrows()


        case 0:
            exit()