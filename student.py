class StudentManager:
    def __init__(self, *args, **kwargs):
        self.students: list = []  # It is a list where in each index it stores a dictionary

    def add_student(self):
        email = input("Enter student email: ")
        if any(s['Email'] == email for s in self.students):
            print("Student with this email already exists!\n")
            return
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        if not age.isdigit():
            print("Invalid age. Please enter a number.\n")
            return
        grade = input("Enter student grade: ")
        
        student_info = {
            "Email": email,
            "Name": name, 
            "Age": age, 
            "Grade": grade
        }
        self.students.append(student_info)
        print("Student added successfully!\n")

    def display_students(self):
        if not self.students:
            print("No students to display.\n")
            return

        print("\nStudent Details:")
        for idx, student in enumerate(self.students, start=1):
            print(f"{idx}. Email: {student['Email']}, Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}")
        print()

    def remove_student(self):
        if not self.students:
            print("No students to remove.\n")
            return

        email = input("Enter student email to remove: ")
        for idx, student in enumerate(self.students, start=1):
            if student['Email'] == email:
                del self.students[idx - 1]
                print(f"Student {email} removed successfully!\n")
                return
        print(f"No student found with the name {email}.\n")

    def update_student(self):
        if not self.students:
            print("No students to update.\n")
            return

        email = input("Enter student email to update: ")
        for student in self.students:
            if student['Email'] == email:
                email = input("Enter student email to update: ")
                new_name = input("Enter new name (leave blank to keep current): ")
                new_age = input("Enter new age (leave blank to keep current): ")
                new_grade = input("Enter new grade (leave blank to keep current): ")

                if email:
                    student['Email'] = email
                if new_name:
                    student['Name'] = new_name
                if new_age and new_age.isdigit():
                    student['Age'] = new_age
                if new_grade:
                    student['Grade'] = new_grade

                print(f"Student {email} updated successfully!\n")
                return
        print(f"No student found with the name {email}.\n")
    
    def search_student(self):
        if not self.students:
            print("No students to search.\n")
            return

        email = input("Enter student email to search: ")
        for student in self.students:
            if student['Email'] == email:
                print(f"Student found: Email: {student['Email']}, Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}\n")
                return
        print(f"No student found with the name {email}.\n")


def main():
    manager = StudentManager()
    
    while True:
        print("1. Add Student")
        print("2. Display Students")
        print("3. Remove Student")
        print("4. Update Student")
        print("5. Search Student")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.display_students()
        elif choice == "3":
            manager.remove_student()
        elif choice == "4":
            manager.update_student()
        elif choice == "5":
            manager.search_student()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
