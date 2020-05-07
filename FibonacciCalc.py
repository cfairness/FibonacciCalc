from math import sqrt  # import sqrt from math library -- since we only need sqrt, no need to import with *


def fibCalc(nthNum):  # function definition to calc Nth number in sequence, adapted from Binet's formula
    fibNum = (1/sqrt(5)) * (((1+sqrt(5))/2)**nthNum - ((1-sqrt(5))/2)**nthNum)  # calculate nth number
    return int(round(fibNum, 0))  # return result rounded to 0 places


def main():  # main method begins
    print("This program computes the nth number in the Fibonacci sequence.")  # introduces the program to the user
    userNum = int(input("Enter the value of n: "))  # prompt user for nth value to calculate

    print("The", str(userNum) + "th", "number in the Fibonacci sequence is", str(fibCalc(userNum)) + ".")
    # print result for user as well as initial entry, using fibCalc function in print statement
    input("Press any key to exit.")  # require user input before the program exits


main()  # main method ends
