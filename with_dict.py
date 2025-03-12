books  = {}
persons = {}
borrows = {}

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
            if any(code == k for k in books.keys()):
                print("code already used")
            else:
                name = input("Enter book name : ")
                books[code] = {"name" : name}


        # show books
        case 2:
            if not books:
                print("There is no book")
            else:
                for key,value in books.items():
                    print(f"code = {key}, name = {value['name']}")

        # remove book
        case 3:
            for key, value in books.items():
                print(f"code = {key}, name = {value['name']}")
            code = input("enter book code that you wants to remove : ")
            if code in books:
                del books[code]
                print("book deleted successfully")
            else:
                print("book not found")

        # edit book
        case 4:
            for key, value in books.items():
                print(f"code = {key}, name = {value['name']}")
            code = input("enter book code that you wants to edit : ")
            if code in books:
                new_name = input("Enter new book name : ")
                books[code] = {"name" : new_name}
                print("person edited successfully")
            else:
                print("book not found")


        # add person
        case 5:
            code = input("Enter person code : ")
            if any(code == k for k in persons.keys()):
                print("code already used")
            else:
                name = input("Enter person name : ")
                family = input("Enter person family name :  : ")
                persons[code] = {"name" : name, "family" : family}
                print("person added successfully")


        # show persons
        case 6:
            if not persons:
                print("there is no person")
            else:
                for k,v in persons.items():
                    print(f"code = {k},name = {v['name']+ ' ' + v['family']}")

        # remove person
        case 7:
            for k, v in persons.items():
                print(f"code = {k},name = {v['name'] + ' ' + v['family']}")
            code = input("enter person code that you wants to remove : ")
            if code in persons:
                del persons[code]
                print("person deleted successfully")
            else:
                print("person not found")

        # edit person
        case 8:
            for k, v in persons.items():
                print(f"code = {k},name = {v['name'] + ' ' + v['family']}")
            code = input("enter person code that you wants to remove : ")
            if code in persons:
                new_name = input("Enter person new name : ")
                new_family = input("Enter person new family name : ")
                persons[code] = {"name": new_name, "family": new_family}
                print("person edited successfully")
            else:
                print("person not found")

        # barrow book
        case 9:
            print("Persons:")
            for k, v in persons.items():
                print(f"code = {k}, full_name = {v['name']} {v['family']}")

            person_code = input("Enter person code that you want to remove: ")

            if person_code in persons:
                print("Books:")
                for key, value in books.items():
                    print(f"code = {key}, name = {value['name']}")

                book_code = input("Enter book code that you want to remove: ")

                if book_code in books:
                    borrow_code = input("Enter borrow code: ")
                    borrows[borrow_code] = {
                        "person_name": persons[person_code]["name"] + " " + persons[person_code]["family"],
                        "book_name": books[book_code]["name"]
                    }
                    print("Book borrowed successfully!")
                else:
                    print("We can't find the book! Sorry.")
            else:
                print("We can't find the person! Sorry.")

        # show barrows
        case 10:
           print(borrows)
        case 0:
            exit()