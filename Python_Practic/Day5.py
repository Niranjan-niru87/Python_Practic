#File Handling in Python
# Opening a file in write mode
'''file = open("example.txt", "w")



# Writing data to the file
file.write("Hello, World!\n")
file.write("Welcome to file handling in Python.\n")



# Closing the file
file.close()



# Opening the file in read mode
file = open("example.txt", "r")




# Reading data from the file
content = file.read()
print(content)



# Closing the file
file.close()



# Appending data to the file
file = open("example.txt", "a")
file.write("This line is appended to the file.\n")
file.close()



# Reading the updated file
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()



# Using 'with' statement to handle files
with open("example.txt", "r") as file:
    content = file.read()
    print("Using 'with' statement:")
    print(content)
# This automatically closes the file after the block



# Checking if the file exists
import os
if os.path.exists("example.txt"):
    print("The file exists.")
else:
    print("The file does not exist.")



# Deleting the file
os.remove("example.txt")
print("The file has been deleted.")



# Verifying deletion
if not os.path.exists("example.txt"):
    print("The file has been successfully deleted.")
# End of File Handling example'''



'''file=open("text.txt", "w")
file.write("Niru\n")
file.close()
file=open("text.txt", "r")
content=file.read()
print(content)'''


'''import csv

with open("student.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)'''


file=open("student.txt","w")
file.write("Name:niru,Marks:90")
file.write("\nName:snipe,Marks:85")
file.close()
file=open("student.txt","r")
content=file.read()
print(content)
