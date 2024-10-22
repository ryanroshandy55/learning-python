# example of function for boolean
class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))


# simple def funciton
def myfunc():
    return True

print(myfunc())


# Function for returning yes or no
def my_func():
    return True

if my_func():
    print("Yes")
else:
    print("No")
    

# instance as boolean
x = 200
print(isinstance(x, int))