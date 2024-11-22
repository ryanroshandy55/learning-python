# pip is a command in terminal that have function to download and install external package that not include in internal py program to use for our program in python 
# This leaks to operate and call directory using import packages

# Check this out in terminal, have your pip connect to terminal?
# pip --version


# for example
# ! run it in your terminal
# pip install camelcase

# import the package
import camelcase

    # print(dir(camelcase))

# used of camelcase
c = camelcase.CamelCase()
txt = "hello world!"
print(c.hump(txt))

# Find packages
# Find more packages at https://pypi.org/.

# Remove a package
# pip uninstall camelcase

# Check list of packages
# pip list