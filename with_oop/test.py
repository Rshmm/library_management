from manage_library import *

persons_manager = PersonManagement()


p1 = persons_manager.add_person(1,"arsham","Hajeb")
p2 = persons_manager.add_person(2,"a","b")
p3 = persons_manager.add_person(3,"c","d")
p4 = persons_manager.add_person(1,"arsham","Hajeb")

persons_manager.show_person()

persons_manager.remove_person(1)

persons_manager.show_person()

persons_manager.edit_person(2,"arsham","Hajeb")

persons_manager.show_person()
