'''
Task Description:
Develop a simple average calculator program. The program requirement is as follows:
1. Allow users to run your program with three input arguments by passing three 
   values to the program: a, b and c.

2. Your program will read the three arguments and calculate the average value.

3. After user inputs all the numbers, if the input numbers are invalid, you need to 
   present an error message "Your input is invalid!". Otherwise, you need to print 
   out the average value. The output average value requires to have 2 precisions. 
   For instance, if the value is 23.456, it should print 23.46. If it is 23, 
   it should print 23.00.
   
NOTE: You have to strictly follow the input and output format.

Running example:
Assume your program is named as AverageCalculator.py. Example output is as follows:

C:\INF1002\Lab1\AverageCalculator>python AverageCalculator.py 3 4 5
Average:4.00

C:\INF1002\Lab1\AverageCalculator>python AverageCalculator.py 60 39 92
Average:63.67

C:\INF1002\Lab1\AverageCalculator>python AverageCalculator.py abc 10 20
Your input is invalid!
'''
import sys

def AverageCalculator():
    # Check if exactly 3 arguments are passed
    if len(sys.argv) != 4:
        print("Your input is invalid!")
        return
    
    try:
        # Convert the input arguments to floats
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
        
        # Calculate the average
        average = (a + b + c) / 3
        
        # Round up to two decimal places
        rounded_average = round(average * 100,2) / 100 # --> The ceil function and the floor function have different definitions. The ceil function returns the smallest integer value which is greater than or equal to the specified number, whereas the floor function returns the largest integer value which is less than or equal to the specified number.
        
        # Print the average rounded to 2 decimal places
        print(f"Average:{rounded_average:.2f}")
    
    except ValueError:
        # Handle non-numeric input
        print("Your input is invalid!")

if __name__ == '__main__':
    AverageCalculator()