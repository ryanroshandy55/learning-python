# Python Iterators
# An iterator is an object that contains a countable number of values,
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values
# Technically, in Python, an iterator is an object which implements the iterator protocolm which consist of the methods __iter__() and __next__()

# Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

# All these object have a iter() method which is used to get an iterator:
# Return an iterator from a tuple, and print each value:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

print("============")

for x in mytuple:
    print(x)

print("============")

# string are iterable objects and can return an iterator
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print("============")

# Looping throught iterator
for x in mystr:
    print(x)

print("============")

# Create an Iterator

# To create an object.class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# As you have learned in the PYTHON CLASSES/OBJECTS chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created
# The __iter_() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print("============")

# Stop Iteration

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)