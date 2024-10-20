# #1
# class Person:
#     # @classmethod
#     def show_details(cls):
#         print(f"Running from {cls.__name__} class.")
#     show_details = classmethod(show_details)


# Person.show_details()

# #2
# class Container:
#     @classmethod
#     def show_details(cls):
#         print(f"Running from {cls.__name__} class.")

# container = Container()
# container.show_details()

class Person:
    instances = []

    # def __init__(self):
    #     Person.instances.append(self)
    
    def __init__ (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Person.instances.append(self)


    @classmethod
    def count_instances(cls):
        return len(Person.instances)

# p1 = Person()
# p2 = Person()
# p3 = Person()
person1 = Person('John', 'Doe')
person2 = Person('Mike', 'Smith')
print(person1.count_instances())