my_dict = {
    "Food" : 0,
    "Travelling" : 0,
    "Rent" : 0,
    "Petrol": 0
}
to_Continue = True

def else_case():
    print("Do you want to continue?")
    print("Enter 1 : For yes")
    print("Enter 2 : For no!")
    user_input_for_exit = input()
    if(validate_input(user_input_for_exit)):
        switch_case_else(int(user_input_for_exit))

def total_expenses():
    sum = 0
    for value in my_dict.values():
        sum = sum + (value)
    print(f"Your total expense is {sum}")

def validate_input(input):
    try:
        int(input)
        return True
    except ValueError:
        print("Enter numbers only!")
        return False

def displayCategories(dict):
    num = 1
    for key,value in dict.items():
        print(f"{num} : {key} : {value}")
        num = num + 1


def add_category_expense(value):
    input_amount = int(input("Enter the amount :"))
    match value:
        case 1:
            my_dict["Food"] = my_dict["Food"] + input_amount
        case 2:
            my_dict["Travelling"] = my_dict["Travelling"] + input_amount
        case 3:
            my_dict["Rent"] = my_dict["Rent"] + input_amount
        case 4:
            my_dict["Petrol"] = my_dict["Petrol"] + input_amount
        case _:
            print("Enter number between the categories number")

def switch_cases(value):
    match value:
        case 1:
            displayCategories(my_dict)
            print("Enter the category number :- ")
            take_input = input()

            if(validate_input(take_input)):
                add_category_expense(int(take_input))
        case 2:
            displayCategories(my_dict)
        case 3:
            total_expenses()
        case 4:
            else_case()
        case _: print("Enter a valid number!")

def switch_case_else(value):
    global to_Continue
    match value:
        case 1 :
            print("Continuing!")
        case 2 :
            print("Exiting! Thanks!")
            to_Continue = False