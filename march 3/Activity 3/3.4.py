def display_student_info():
    try:
        file = open ("students.txt","r")
        print("Reading Student Information.")
        for line in file:
            print(line, end=" ")
            file.close()
    except FileNotFoundError:
        print("File not found")
        
display_student_info()