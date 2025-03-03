import json

FILE_PATH = "records_data.json"

def main():
    data = load_data()

    while True:
        print("\n--- Student Record Management ---")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            data = load_data()
            print("File opened.")
        elif choice == "2":
            save_data(data)
            print("File saved.")
        elif choice == "3":
            save_data(data, input("Enter new file name: "))
            print("File saved as new file.")
        elif choice == "4":
            display_data(data)
        elif choice == "5":
            data = sort_by_lastname(data)
            print("Sorted by last name.")
        elif choice == "6":
            data = sort_by_grade(data)
            print("Sorted by grade.")
        elif choice == "7":
            stud_id = input("Enter Student ID: ")
            student = find_student(data, stud_id)
            print(student if student else "Student not found.")
        elif choice == "8":
            insert_entry(data)
        elif choice == "9":
            modify_entry(data)
        elif choice == "10":
            remove_entry(data)
        elif choice == "11":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")

def load_data():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data, filename=FILE_PATH):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def compute_final_score(standing, exam_score):
    return round((standing * 0.6) + (exam_score * 0.4), 2)

def display_data(data):
    if not data:
        print("\nNo student records available.")
        return
    for entry in data:
        final_score = compute_final_score(entry[2], entry[3])
        print(f"ID: {entry[0]}, Name: {entry[1][0]} {entry[1][1]}, Final Grade: {final_score}")

def sort_by_lastname(data):
    return sorted(data, key=lambda x: x[1][1])

def sort_by_grade(data):
    return sorted(data, key=lambda x: compute_final_score(x[2], x[3]), reverse=True)

def find_student(data, stud_id):
    return next((entry for entry in data if entry[0] == stud_id), None)

def insert_entry(data):
    stud_id = input("Enter Student ID: ")
    fname, lname = input("Enter First Name: "), input("Enter Last Name: ")
    standing, exam_score = float(input("Class Standing: ")), float(input("Exam Score: "))
    data.append((stud_id, (fname, lname), standing, exam_score))
    print("Entry Added!")

def modify_entry(data):
    stud_id = input("Enter Student ID to Edit: ")
    student = find_student(data, stud_id)
    if student:
        data.remove(student)
        insert_entry(data)
        print("Entry Updated!")
    else:
        print("Student not found.")

def remove_entry(data):
    stud_id = input("Enter Student ID to Delete: ")
    student = find_student(data, stud_id)
    if student:
        data.remove(student)
        print("Entry Deleted!")
    else:
        print("Student not found.")

if __name__ == "__main__":
    main()