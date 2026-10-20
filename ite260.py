students = []

while True:
    print("\n=== STUDENT ATTENDANCE SYSTEM ===")
    print("1. Add Student Attendance")
    print("2. View Attendance")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter students' name: ")
        status = input("Enter status (Present/Absent/Late): ")

        students.append({
            "name": name,
            "status": status
        })

        print("Attendance recorded successfully!")

    elif choice == "2":
        print("\n=== Attendance Records ===")

        for student in students:
            print(student["name"], "-", student["status"])

    elif choice == "3":
        print("===Finishing the Attendance===")
        break

    else:
        print("Invalid choice. Try again.")
