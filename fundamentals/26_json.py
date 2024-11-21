# Python JSON
# JSON is a syntax for storing and exchanging data
# JSON is text, written with JavaScript object notation

import json

# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method

# some JSON, JSON looks like a dictionary (but it have single quets before the curve brackets)
x = '{"name": "john", "age" : 30, "city": "New York"}'

# parse x:
y = json.loads(x)

# The result is a Python dictionary
print(y['age'])


# Convert from Python to JSON:

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x)

# The result is a JSON string:
print(y)

# You can convert Python objects of the following types, into JSON strings:

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

# Example
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Convert a Python object containing all the legal data types:
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# print(json.dumps(x))

# Format the Result
# print(json.dumps(x, indent=2))

# print(json.dumps(x, indent=1, separators=(". ", " = ")))

# Order the result
print(json.dumps(x, indent=4, sort_keys=True))