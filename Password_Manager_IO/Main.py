import random
import string

password_file = "passwordFile.txt"

def generation_method(length = 6):
    chooseFrom = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chooseFrom) for _ in range(length))

def save_password(site,username,password):
    file = open("passwordFile.txt",'a')
    file.write(f"{site},{username},{password}\n")
    print(f"Password saved for {site}")
    file.close()

def show_password():
    file = open("passwordFile.txt",'r')
    for aLine in file:
        print(aLine.strip().split(','))

while(True):
    print("1 : Generate password!")
    print("2 : Store password!")
    print("3 : Display all passwords")
    print("4 : Exit")
    choice = input("Input your choice: ")

    if choice =="1":
        print(generation_method())
    elif choice == "2":
        site = input("Enter the site name")
        username = input("Enter username")
        password = input("Enter password")
        save_password(site,username,password)
    elif choice == "3":
        show_password()
    elif choice == "4":
        print("Exiting! thanks!")
        break
    else:
        print("Enter number between 1 to 4")
