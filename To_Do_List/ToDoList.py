#To do list app:

tasks = []

def isvalidInput(num):
    try:
        int(num)
        return True

    except ValueError:
        print("Enter numbers only")
        return False


def displayList():
    for i in range(len(tasks)):
        print(f"Task {i+1} : {tasks[i]}")

def validateTasks(num):
    if(isvalidInput(num)):
        num = int(num)
        if (num >= 1 and num <= len(tasks)):
            tasks.pop(num-1)
            print("Task removed!")
        else:
            print("Enter a task number between your tasks number")
    else:
        print("Enter an integer only!")

toContinue = True

while(toContinue):

    print("Enter 1: To add a task")
    print("Enter 2: To remove a task")
    print("Enter 3: To view the tasks")
    print("Enter 4: To exit")

    user_input = input()

    if (isvalidInput(user_input)):
        user_input = int(user_input)
        if (user_input == 1):
            task_input = input("Enter your task")
            tasks.append(task_input)
            print("Task added Successfully!")

        elif (user_input == 2):
            displayList()
            task_input = input("Enter the task number you want to remove")
            validateTasks(task_input)

        elif (user_input == 3):
            displayList()
        elif (user_input == 4):
            print("Exiting...")
            toContinue = False
        else:
            print("Enter a number between 1 to 4")