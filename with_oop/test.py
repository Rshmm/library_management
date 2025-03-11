from manage_library import *

# persons_manager = PersonManagement()

person_manager = PersonManagement()
book_manager = BookManagement()

p1 = person_manager.add_person(1,"arsham","Hajeb")
p2 = person_manager.add_person(2,"a","b")
p3 = person_manager.add_person(3,"c","d")
p4 = person_manager.add_person(1,"arsham","Hajeb")

# persons_manager.show_person()
#
# persons_manager.remove_person(1)
#
# persons_manager.show_person()
#
# persons_manager.edit_person(2,"arsham","Hajeb")

# persons_manager.show_person()
#
#
#
# book_manager = BookManagement()

b1 = book_manager.add_book(1,"a")
b2 = book_manager.add_book(2,"b")
b3 = book_manager.add_book(3,"c")
b4 = book_manager.add_book(1,"a")

# book_manager.show_book()
#
# book_manager.remove_book(1)
#
# book_manager.show_book()
#
# book_manager.edit_book(2,"a")
#
# book_manager.show_book()


manager = Borrow(person_manager,book_manager)
manager.borrow_book(1,2)
manager.show_borrows()