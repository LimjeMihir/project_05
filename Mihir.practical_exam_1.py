
class Schedule:
    
    def __init__(self,taskid,title,description,date,priority,status):
        
         self.taskid= taskid
         self.title = title
         self.description = description
         self.date = date
         self.priority = priority
         self.status = status

    def view_task(self):
        if not self.taskid:
            print("No task available.")
            return

    def update_task(self,taskid,title,description,date,priority,status):
        if task_id not in self.taskid:
            print("task not found")
            return
        
        print(f"Task updated successfully!")

    def delete_task(self,taskid,title,description,date,priority,status):
        if taskid in self.taskid:
            del self.taskid
            print(f"task {taskid} deleted successfully!")
        else:
            print("task not found.")
    

task={}

taskid=''
title=''
description=''
date=''
priority=''
status=''

while True:
    print("welcome to the Task Scheduler Application")
    print("\n1. Add a new task")
    print("2. view all tasks")
    print("3. Edit a task")
    print("4. delete a task")
    print("5. sort tasks by pripority or due date")
    print("6. Filter task by status")
    print("7. show summary statisticas")
    print("8. Exit")

    choice=int(input("enter your choice:"))

    if choice == 1:
        taskid=int(input("Enter Task Id:"))
        title=input("Enter Title:")
        description=input("Enter Description:")
        date=input("Enter Due date (DD/MM/YY):")
        priority=input("Enter Priority (High/Medium/Low):")
        status=input("Enter Status(pending/completed):")

        print("/nTask added successfully!")

        sel=input("do you want to continue? (y/n):")

        if sel == 'y':
            continue
        
        elif sel == 'n':
            print("thank you for using Task scheduler application!goodbye")
            break
        else:
             print("please Try again!")


    if choice == 2:
        print(task)
        
        sel=input("do you want to continue? (y/n):")
        
        if sel1 == 'y':
            continue
        
        elif sel2 == 'n':
            print("thank you for using Task scheduler application!goodbye")
            break
        else:
             print("please Try again!")

    if choice == 3:
        taskid=int(input("Enter Task Id:"))
        title=input("Enter Title:")
        description=input("Enter Description:")
        date=input("Enter Due date (DD/MM/YY):")
        priority=input("Enter Priority (High/Medium/Low):")
        status=input("Enter Status(pending/completed):")
        pass

    if choice == 4:
        task_id=int(input("enter task id to delete:"))
        pass

    if choice == 5:
        pass

    if choice == 6:
        pass

    if choice == 7:
        pass

    if choice == 8:
        print("Exiting the program!Thankyou visit again")

        break

    else:
        print("Invalid choice! please try again")
        
    
