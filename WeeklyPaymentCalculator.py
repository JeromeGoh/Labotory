'''
Task Description:
Develop one employee weekly payment calculation program as we have discussed in 
Lecture 2. The program requirement is as follows: 
1.	Allow users to run your program with three input arguments by passing three
    values to the program:  the number of working hours, input normal rate and 
    input the overtime rate.

2.	Your program will read the three arguments and calculate the users salary 
    using the following two formulas:
        a.	Payment of the normal hours = normal rate * normal hours
        b.	Payment of the overtime hours = overtime rate * overtime hours
        NOTE: the working hours within 40 belong to normal hours and those beyond 
              40 hours are considered as overtime hours. 

3.	After user inputs all the numbers, if the input numbers are invalid, you need 
    to present an error message "Your input is invalid!". Otherwise, you need to 
    print out the employee's payment of normal hours, his payment of overtime 
    hours and total payment. The output payment requires to have 2 precisions. 
    For instance, if payment is 2300.456, it should print 2300.46. 
    If payment is 2300, it should print 2300.00.
      
NOTE: You have to strictly follow the input and output format. 

Running example:
Assume your program is named as WeeklyPaymentCalculator.py. Example output is as follows: 

C:\INF1002\Lab1\WeeklyPaymentCalculator> python weeklyPaymentCalculator.py 20 30 100
Normal Salary:600.00, Extra Salary:0.00, Total Salary:600.00

C:\INF1002\Lab1\WeeklyPaymentCalculator> python weeklyPaymentCalculator.py 60 30 200
Normal Salary:1200.00, Extra Salary:4000.00, Total Salary:5200.00

C:\INF1002\Lab1\WeeklyPaymentCalculator> python weeklyPaymentCalculator.py 10000 10 200
Your input is invalid!

'''
import sys

def WeeklyPaymentCalculator():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Your input is invalid!")
        return
    
    try:
        # Parse input arguments
        working_hours = float(sys.argv[1])
        normal_rate = float(sys.argv[2])
        overtime_rate = float(sys.argv[3])
        
        # Validate inputs
        if working_hours < 0 or normal_rate < 0 or overtime_rate < 0 or working_hours > 168:  # 168 hours is max possible in a week
            print("Your input is invalid!")
            return

        # Calculate normal and overtime hours
        normal_hours = min(working_hours, 40)
        overtime_hours = max(0, working_hours - 40)
        
        # Calculate normal and overtime payment
        normal_salary = normal_hours * normal_rate
        extra_salary = overtime_hours * overtime_rate
        total_salary = normal_salary + extra_salary
        
        # Print salaries with two decimal precision
        print(f"Normal Salary:{normal_salary:.2f}, Extra Salary:{extra_salary:.2f}, Total Salary:{total_salary:.2f}")
    
    except ValueError:
        # Catch any conversion errors
        print("Your input is invalid!")

if __name__ == '__main__':
    WeeklyPaymentCalculator()