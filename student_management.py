import csv
import os

file_name = "students.csv"
if not os.path.exists(file_name):
    with open(file_name,"w",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID","Name","Age","Course"])

print("CSV File Ready!")

def add_student():
    id = input("Enter Student ID: ")

    with open(file_name,"r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == id:
                print("ID already exists!")
                return
            
    name = input("Enter Name: ")

    while True:
        age = input("Enter Age: ")

        if age.isdigit():
            break
        else:
            print("Age must be a number!")

    course = input("Enter Course: ")

    with open(file_name,"a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([id, name, age, course])

    print("Student added successfully!") 

def view_students():
    with open(file_name,"r") as file:
        reader = csv.reader(file)

        print("n---Student List---")

        for row in reader:
            print(f"ID:{row[0]}, Name: {row[1]}, Age:{row[2]}, Course:{row[3]}")

def search_student():
    search_id = input("Enter Student ID to search: ")

    found = False
    with open(file_name,"r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == search_id:
                print("\n---Student Found---")
                print(f"ID:{row[0]}, Name:{row[1]}, Age:{row[2]}, Course:{row[3]}")
                found = True
                break

        if not found:
                print("Student not found.") 

def update_student():
    update_id = input("Enter Student ID to update: ")

    updated_rows = []
    found = False

    with open(file_name,"r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == update_id:
                print("\nEnter new details: ")

                name = input("Enter New Name: ")
                age = input("Enter New Age: ")
                course = input("Enter New Course: ")

                updated_rows.append([update_id,name,age,course])
                found = True

            else:
                updated_rows.append(row)

    if found:   
        with open(file_name,"w",newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)     

        print("Student Updated Successfully!")

    else:
        print("Student ID not found.")           

def delete_student():
    delete_id = input("Enter Student ID to delete: ")

    updated_rows = []
    found = False

    with open(file_name,"r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == delete_id:
                found = True
                print("Student Deleted Successfully!")
            else:
                updated_rows.append(row)

    if found:
        with open(file_name,"w",newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)
    else:
        print("Student ID not found.")

def count_students():
    with open(file_name,"r") as file:
        reader = csv.reader(file)
        count = -1

        for row in reader:
            count += 1

            print("Total Students:",count)

while True:
    print("\n---Student Management System---") 
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Count Students")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        count_students()

    elif choice == "7":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")


