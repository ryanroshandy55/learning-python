# Returns a 6-element string. This will be the value of the bookid
# attribute.

# Using the above code, create a static method of the Book class (use the
# @staticmethod decorator) called get_id() L which will generate a 6-
# digit str object (the value of the bookid field).
# Then create an instance of the class named book1 with the following

# arguments:
# • title=' Python Object Oriented Programming Exercises Volume 2'
# • author='Edcorner Learning'
# In response, print all the _dict_ attribute keys of book1 to the console.
# dict_keys = (['book_id', 'title','author'])


# import uuid

# class Book:
#     def __init_(self, title, author):
#         self.book_id = self.get_id()
#         self.title = title
#         self.author = author

#     def __repr__(self):
#         return f"Book(title='{self.title}', author='{self.author}')"

#     @staticmethod
#     def get_id():
#         return str(uuid.uuid4().fields[-1])[:6]

# # book1 = Book("Python Object Oriented Programming Exercises Volume 2", "Edcorner Learning")
# book1 = Book('Python Object Oriented Programming Exercises Volume 2', 'Edcorner Learning')
# # print(book1.__dict__.keys())
# print(book1)

import uuid

class Book:
    def __init__(self, title, author):
        self.book_id = self.get_id()
        self.title = title
        self.author = author
    
    def __repr__(self):
        return f"Book(title='{self.title}, author='{self.author}')"
    
    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]
    
book1 = Book('Python Object Oriented Programming Exercises Volume', 'Edcorner Learning')
print(book1)

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f"Person(fname = '{self.fname}', lname = '{self.lname}')"

    def __str__(self):
        return f"First name: {self.fname}\nLast name: {self.lname}"

person = Person('Ryan','Roshandy')
print(person)