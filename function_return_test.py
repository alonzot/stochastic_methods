#This program uses a function to square a number from user input
#Programmer: Tony T
#Language: Python 3.4

def main():
    #create and initialize variables and constants
    number=0.0
    number_squared=0.0
    #input - get the number to square
    number=float(input("Please enter the number to square "))
    #process - call the function
    number_squared=square_number(number)
    #output- display the results
    print("the square of ", number, "is", format(number_squared, '0.2f'))

def square_number(number):
    #create and initialize variables and constants
    square=0.0
    #process - compute square of number
    square = number**2
    return square
         
#call the main() function
main()
