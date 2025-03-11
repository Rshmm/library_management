from intanses_of_library import Person,Book

class PersonManagement:
    def __init__(self):
        self.persons = []



    def add_person(self,code,name,family):
        if any(code == person.code for person in self.persons):
            print("code already used")
        else:
            self.persons.append(Person(code,name,family))
            print("person added successfully")

    def show_person(self):
        print("Persons")
        for person in self.persons:
            print(person)

    def remove_person(self,code):
        found = False
        for person in self.persons:
            if code == person.code:
                found = True
                self.persons.remove(person)
                print("person removed successfully")

        if not found:
            print("person dose`nt exist")



    def edit_person(self,code,new_name,new_family):
        found = False
        for person in self.persons:
            if code == person.code:
                found = True
                person.name = new_name
                person.family = new_family
                print("person edited successfully")
        if not found:
            print("person dose`nt exist")




class BooManagement:

    def __init__(self):
        self.books = []


    def add_book(self,code,name):
        if any(code == book.code for book in self.books):
            print("code already used")
        else:
            self.books.append(Book(code,name))
            print("book added successfully")

    def show_book(self):
        for book in self.books:
            print(book)


    def remove_book(self,code):
        found = False
        for book in self.books:
            if code == book.code:
                found = True
                self.books.remove(book)
                print("book removed successfully")
        if not found:
            print("book dose`nt exist")


    def edit_book(self,code,new_name):
        found = False
        for book in self.books:
            if code == book.code:
                found = True
                book.name = new_name
                print("book edited successfully")
        if not found:
            print("book dose`nt exist")



















