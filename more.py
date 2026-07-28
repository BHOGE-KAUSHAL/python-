# Exception and file handling
# a = int(input("provide your number :-"))
# b = int(input("provide your number :-"))

# try:
#     print(a/b)
# except Exception as err:
#     print(f"sorry an error occured as {err}")
# else:
#     print("there was no error ")    
# print(a+b) 


# file handling

# file = open("class6.py")
# print(file.read())


# 'r' -for reading the file .error if file does not exist 
# 'a' - for appending in file .creates a file as well
# 'w' - overwriting the file.create if it does not exist
# 'x' - create a file.error if file already exist

# open('pull.txt','x')
# file =open ("push.txt","a")
# file.write("hello this is a sample file that i have created ")
# file.close()

with open("class6.py",'r') as fs:
    print(fs.read())