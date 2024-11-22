# Read Lines
f = open(r"fundamentals\32_file_handling\demofile.txt", "r")
print(f.read(), "\n")

print(f.read(5), "\n")

# Read one line of the file:
f = open(r"fundamentals\32_file_handling\demofile.txt", "r")
print(f.readline(), "\n")

# By calling readline() two times, you can read the two first lines:
f = open(r"fundamentals\32_file_handling\demofile.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())

# Looping through the lines of the file, you can read the whole file, line by line
f = open(r"fundamentals\32_file_handling\demofile.txt", "r")
for x in f:
    print(x)
f.close()