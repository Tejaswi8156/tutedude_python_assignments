# Task 8: Write and Append Data to a File

# Writing data to the file
text = input("Enter text to write to the file: ")
file = open("output.txt", "w")
file.write(text + "\n")
file.close()
print("Data successfully written to output.txt.")

# Appending data to the file
append_text = input("Enter additional text to append: ")
file = open("output.txt", "a")
file.write(append_text + "\n")
file.close()
print("Data successfully appended.")

# Reading and displaying final content
print("Final content of output.txt:")
file = open("output.txt", "r")
print(file.read())
file.close()
