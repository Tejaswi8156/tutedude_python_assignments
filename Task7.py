# Task 7: Read a File and Handle Errors

try:
    file = open("sample.txt", "r")
    print("Reading File Content:")

    line_number = 1
    for line in file:
        print(f"Line {line_number} : {line.strip()}")
        line_number += 1

    file.close()

except FileNotFoundError:
    print("Error: the file named 'sample.txt' wasn't found.")
