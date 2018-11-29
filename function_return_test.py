# This program uses a function to square a number from user input
# Programmer: Tony T
# Language: Python 3.7

def main():
    # create and initialize variables and constants
    number=0.0
    number_squared = 0.0
    # input - get the number to square
    number=float(input("Please enter the number to square "))
    # process - call the function
    number_squared = square_number(number)
    # output- display the results
    print("the square of ", number, "is", format(number_squared, '0.2f'))

    l1=[i for i in range(10)]
    print(square_list(l1))
def square_number(number):
    # create and initialize variables and constants
    square=0.0
    # process - compute square of number
    square = number**2
    return square

def square_list(value_list):
    l2 = [x**2 for x in value_list]
    return l2

         
# call the main() function
if __name__ == '__main__' :
    main()
