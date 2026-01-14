#================================================================= To-Do List Program ===================================================================
class ToDoApp:
    def __init__(self):
        self.tasks=[]

    def generate_id(self):
        return len(self.tasks)+1

    def add_task(self):
        while True:
            task_name=input("Enter Task's Name: ")
            if all(ch.isalpha() or ch.isspace() for ch in task_name):
                break
            else:
                print("Invalid Task Name!")
                continue

        task_description=input("Enter Task Description: ")
        task_status=input("Enter Task Status(Active/Inactive): ")

        task = {
            "ID": self.generate_id(),
            "Task Name": task_name,
            "Task Description": task_description,
            "Task Status": task_status
        }
        self.tasks.append(task)
        print("Task Added Succesfully!\n")

    def display_inactive(self):
        if not self.tasks:
            print("No Tasks available!!")
            return
        for task in self.tasks:
            if(task["Task Status"]=="inactive"):
                print(f"Task ID: {task["ID"]}, Task Name: {task["Task Name"]}, Task Description: {task["Task Description"]}, Task Status: {task["Task Status"]}")

    def display_active(self):
        if not self.tasks:
            print("No Tasks available!!")
            return
        for task in self.tasks:
            if(task["Task Status"]=="active"):
                print(f"Task ID: {task["ID"]}, Task Name: {task["Task Name"]}, Task Description: {task["Task Description"]}, Task Status: {task["Task Status"]}")

    def update_todo(self):
        if not self.tasks:
            print("No tasks to update.\n")
            return

        id = input("Enter task id to update: ")
        for task in self.tasks:
            if task['ID'] == int(id) and task["Task Status"]=='active':
                new_name = input("Enter new Name (leave blank to keep current): ")
                new_description = input("Enter new Description (leave blank to keep current): ")
                new_status = input("Enter new status (leave blank to keep current): ")

                if new_name:
                    task['Task Name'] = new_name
                else:
                    print("No value given, we continue with old Task Name!")
                if new_description:
                    task['Task Description'] = new_description
                else:
                    print("No value given, we continue with old Description!")
                if new_status:
                    task['Task Status'] = new_status
                else:
                    print("No value given, we continue with old Status!")

                print(f"Task {id} updated successfully!\n")
                return
        print(f"No task found with the id {id}.\n")
    
def main():
    app=ToDoApp()
    while True:
        print("------------------To-Do Menu------------------")
        print("1. Add Task")
        print("2. Show Active Tasks")
        print("3. Show Inactive Tasks")
        print("4. Update Tasks")
        print("5. Exit")
        
        while True:
            try:
                choice:int=int(input("Enter Your Choice: "))
                break
            except ValueError:
                print("Invalid Input!!")
                continue
        
        if choice == 1:
            app.add_task()
        elif choice == 2:
            app.display_active()
        
        elif choice == 3:
            app.display_inactive()

        elif choice == 4:
            app.update_todo()

        elif choice == 5:
            print("Exiting...")

        else:
            print("Invalid Choice.!\n")


if __name__ == "__main__":
    main()
