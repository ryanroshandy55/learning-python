f = open("demofile.txt", "w")
f.write("Hello I'm writting this code, \nNice too meet you buddy, i hope we soon meet somewhere")
f.close()

f = open("demofile.txt", "r")
print(f.read())
f.close()


# This command to delete file
import os
os.remove("demofile.txt")

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")
    
# careful with this, if you do wrong delete, your folder will remove permanent    
# os.mkdir("fundamental3")
# os.rmdir("fundamental3")

# os.mkdir("fundamentals/32_file_handling/this_example_folder")

# Every command will create or delete folder, it's just little fun somehow :v
if os.path.exists("fundamentals/32_file_handling/this_example_folder"):
    os.remove("fundamentals/32_file_handling/this_example_folder/file.txt")
    os.rmdir("fundamentals/32_file_handling/this_example_folder")
else:    
    os.mkdir("fundamentals/32_file_handling/this_example_folder")
    f = open("fundamentals/32_file_handling/this_example_folder/file.txt", "x")
    f.close()
    f = open("fundamentals/32_file_handling/this_example_folder/file.txt", "w")
    f.write("Hello this is Me the author")
    f.write("\nI just want to say thank you for all of you who have see this code")
    f.write("\nI hope you have a bright future, and i just want to say, enjoy the process")
    f.close()
    f = open("fundamentals/32_file_handling/this_example_folder/file.txt", "r")
    print(f.read())
    f.close()