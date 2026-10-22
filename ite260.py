students = []

#Main Menu of the attendance
while True:
    print("\n=== STUDENT ATTENDANCE SYSTEM ===")
    print("1. Add Student Attendance")
    print("2. View Attendance")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Inputs date and attendance details and store them in the list
    if choice == "1":
        date = input("Enter date (MM-DD-YYYY): ")
        name = input("Enter students' name: ")
        status = input("Enter status (Present/Absent/Late): ")

        students.append({
            "date": date,
            "name": name,
            "status": status
        })

        print("Attendance recorded successfully!")

    # Displays the attendance of student records stored in the list
    elif choice == "2":
        print("\n=== Attendance Records ===")

        for student in students:
            print(student["name"], "-", student["status"], "-",student["date"])

    #Exits the attendance program and breaks the loop
    elif choice == "3":
        print("=== Finishing the Attendance ===")
        break
    
    #If user puts different choice than the given options, will print invalid
    else:
        print("Invalid choice. Try again.")
        
