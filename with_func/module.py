books = []
persons = []
borrows = []


def add_book(code, name):
    if any(code == book[0] for book in books):
        print("code already used")
    else:
        return books.append([code, name])
    print("book added successfully")


def show_books():
    for book in books:
        print(f"code = {book[0]} , name = {book[1]}")


def remove_book(code):
    found = False
    for book in books:
        if code == book[0]:
            found = True
            books.remove(book)
            print("book removed successfully")
    if not found:
        print("book does`nt exist")


def edit_book(code, new_name):
    found = False
    for book in books:
        if code == book[0]:
            found = True
            book[1] = new_name
            print("book edited successfully")
    if not found:
        print("book does`nt exist")


def add_person(code, name, family):
    if any(code == person[0] for person in persons):
        print("code already used")
    else:
        persons.append([code, name, family])
        print("person added successfully")


def show_persons():
    for person in persons:
        print(f"code = {person[0]} , name = {person[1] + ' ' + person[2]}")


def remove_person(code):
    found = False
    for person in persons:
        if code == person[0]:
            found = True
            persons.remove(person)
            print("person removed successfully")
    if not found:
        print("person does`nt exist")


def edit_person(code, new_name, new_family):
    found = False
    for person in persons:
        if code == person[0]:
            found = True
            person[1] = new_name
            person[2] = new_family
            print("person edited successfully")
    if not found:
        print("person does`nt exist")


def borrow_book(code_person, code_book):
    found = False
    for person in persons:
        if code_person == person[0]:
            found = True
            for book in books:
                if code_book == book[0]:
                    found = True
                    borrows.append([book[1], person[1], person[2]])
                    print("book borrowed successfully")
            if not found:
                print("book does`nt exist")
    if not found:
        print("person does`nt exist")


def show_borrows():
    for borrow in borrows:
        print(f"{borrow[1] + ' ' + borrow[2]} borrowed book {borrow[0]}")
