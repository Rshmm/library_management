books = []
persons = []
borrows = []

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
            if any(code == book[0] for book in books):
                print("code already used")

            else:
                name = input("Enter book name : ")
                books.append([code,name])

        # show books
        case 2:
            for book in books:
                print("books")
                print(f"code = {book[0]} , name = {book[1]}")

        # remove book
        case 3:
            for book in books:
                print("books")
                print(f"code = {book[0]} , name = {book[1]}")
            code = input("Enter book code that you want to remove : ")
            found = False
            for book in books:
                if code == book[0]:
                    found = True
                    persons.remove(book)
                    print("book removed successfully")
            if not found:
                print("we cant find the book! sorry")

        # edit book
        case 4:
            for book in books:
                print("books")
                print(f"code = {book[0]} , name = {book[1]}")
            code = input("Enter book code that you want to edit : ")
            found = False
            for book in books:
                if code == book[0]:
                    found = True
                    new_name = input("enter new book name : ")
                    book[1] = new_name
                    print("book edited successfully")
            if not found:
                print("we cant find the book! sorry")

        # add person
        case 5:
            code = input("Enter person code : ")
            if any(code == person[0] for person in persons):
                print("code already used")
            else:
                name = input("enter person name : ")
                family = input("enter person family name : ")
                persons.append([code,name,family])

        # show persons
        case 6:
            for person in persons:
                print("persons")
                print(f"code = {person[0]} , full_name = {person[1] + ' ' + person[2]}")

        # remove person
        case 7:
            for person in persons:
                print("persons")
                print(f"code = {person[0]} , full_name = {person[1] + ' ' + person[2]}")
            code = input("Enter person code that you want to remove : ")
            found = False
            for person in persons:
                if code == person[0]:
                    found = True
                    persons.remove(person)
                    print("person removed successfully")
            if not found:
                print("we cant find the person! sorry")

        # edit person
        case 8:
            for person in persons:
                print("persons")
                print(f"code = {person[0]} , full_name = {person[1] + ' ' + person[2]}")
            code = input("Enter person code that you want to edit : ")
            found = False
            for person in persons:
                if code == person[0]:
                    found = True
                    new_name = input("Enter new person name :")
                    new_family = input("Enter new person family name  :")
                    person[1] = new_name
                    person[2] = new_family
                    print("person edited successfully")
            if not found:
                print("we cant find the person! sorry")

        # barrow book
        case 9 :
            for person in persons:
                print("persons")
                print(f"code = {person[0]} , full_name = {person[1] + ' ' + person[2]}")
            code = input("Enter person code that you want to remove : ")
            found = False
            for person in persons:
                if code == person[0]:
                    found = True
                    for book in books:
                        print("books")
                        print(f"code = {book[0]} , name = {book[1]}")
                    code = input("Enter book code that you want to remove : ")
                    found = False
                    for book in books:
                        if code == book[0]:
                            found = True
                            borrows.append([person[1],person[2],book[1]])
                            print("book borrowed successfully")
                    if not found:
                        print("we cant find the book! sorry")

            if not found:
                print("we cant find the person! sorry")

        # show barrows
        case 10:
            for borrow in borrows:
                print(f"person = {borrow[0] + ' ' + borrow[1]} borrowed book = {borrow[2]}")
        case 0:
            exit()