file = open ("students.txt", "w")

LN = input("Enter Last name: ")
FN = input("Enter First name: ")
age = input("Enter age: ")
contnum = input("Enter contact number: ")
course = input("Enter course: ")

file.write(f"Last name: {LN}\n")
file.write(f"First name: {FN}\n")
file.write(f"age: {age}\n")
file.write(f"Contact Number: {contnum}\n")
file.write(f"Course: {course}\n")

file.close()
print("Student information has been saved to 'students.txt")
