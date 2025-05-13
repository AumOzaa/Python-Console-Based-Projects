#Personal Tracker for Expenses :
# Would prompt user to add the expense type.
# add the details of it through string and then what would we do is add it in the dictionary
import Methods as methods

while(methods.to_Continue):
    print("Enter 1 :  To add an expense")
    print("Enter 2 :  To view your expenses")
    print("Enter 3 :  To view the total expenses")
    print("Enter 4 :  To Exit")
    user_input = input()
    if (methods.validate_input(user_input)):
        user_input = int(user_input)
        methods.switch_cases(user_input)
    else:
        methods.else_case()

