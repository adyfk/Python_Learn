# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)


# Sample Read Some File
f = open("./Materi/Helper/demofile.txt", "r")
print(f.read())
# Tidak bisa digunakan lagi
print(f.read(5))


f = open("./Materi/Helper/demofile.txt", "r")
print(f.readline())
print(f.readline())
f.close()


# Sample Write / Create File
f = open("./Materi/Helper/demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("./Materi/Helper/demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()


# Sample Delete File

# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")

# os.rmdir("myfolder")
