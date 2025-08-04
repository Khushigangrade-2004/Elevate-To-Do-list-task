Task = []
total = int(input("enter the no. of task you wand to add in Today Task : "))
for i in range(1,total+1):
    add = input(f"enter {i} task : ")
    Task.append(add)
    print(f"'{add}' is successfully added in your today task")
print("YOUR TODAY TASK IS...")
for i ,value in enumerate (Task,start=1):
    print(f"{i}.{value}")

while True:
    choice=input("press the number if you want to.... \n 1. Add New Task\n 2. Delete Existing Task \n 3. Update Task \n 4. View Task list \n 5. Exit :\n")
    if choice == "1":
        Adding=input("Add the task you want to do : ")
        Task.append(Adding)
        print(f"'{Adding}' is successfully added in your today task list")
    elif choice == "2":
        Deleting=input("Delete one task you want to delete : ")
        if Deleting in Task:
            Task.remove(Deleting)
            print(f"'{Deleting}' is successfully deleted in your task list!")
        else:
            print("Task is unavailable in the Task List")
    elif choice =="3":
        Update=input("which task you want to update : ")
        if Update in Task:
            idx=Task.index(Update)
            Task[idx]=input("enter new task : ")
            print("Task list successfully updated")
        else:
            ("Task is unavailable in the Task List")
    elif choice =="4":
        print("Your today task list is....")
        for i,value in enumerate (Task,start=1):
              print(f"{i}. {value}")
    else:
        print("Thanks for using Task List")
        break
        

            
