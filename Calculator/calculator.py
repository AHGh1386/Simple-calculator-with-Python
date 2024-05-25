def calculate():
    number_1 = int(input("Enter your the first number: "))
    number_2 = int(input("Enter your the second number: "))
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')
    if operation == '+':
        output_number = number_1 + number_2
        print( "{} + {} = {}" .format(number_1, number_2, output_number))
    elif operation == '-':
        output_number = number_1 - number_2
        print( "{} - {} = {}" .format(number_1, number_2, output_number))
    elif operation == '*':
        output_number = number_1 * number_2
        print( "{} * {} = {}" .format(number_1, number_2, output_number))
    elif operation == '/':
        output_number = number_1 / number_2
        print( "{} / {} = {}" .format(number_1, number_2, output_number))
    else:
        print('You have not typed a valid operator, please run the program again.')
    again()
# Define again() function to ask user if they want to use the calculator again
def again():
    # Take input from user
    calc_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''')
    # If user types Y, run the calculate() function
    if calc_again.upper() == 'Y':
        calculate()
    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print('See you later.')
    # If user types another key, run the function again
    else:
        again()
# Call calculate() outside of the function
calculate()
