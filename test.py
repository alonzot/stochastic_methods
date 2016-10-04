def add_two(x,y):
    return(x+y)

def multiply_two(x,y):
    return x*y

def subtract(x, y):
    return (x-y)

def main():
    x=float(input("enter the first value "))
    y=float(input("enter the second value "))
    print("The sum of {0:.2f} and {1:.2f} is {2:.2f}".format(x, y, add_two(x,y)))

if __name__ == "__main__":
    main()
