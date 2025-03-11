class Book:
    def __init__(self,code,name):
        self.code =  code
        self.name = name

    def __repr__(self):
        return f"book code = {self.code} , book name = {self.name}"

class Person:
    def __init__(self,code,name,family):
        self.code = code
        self.name = name
        self.family = family

    def __repr__(self):
        return f"person code = {self.code} , person name = {self.name + ' ' + self.family}"
