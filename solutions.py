"""
Practice problems to get the hang of converting among data types.
In this case, we focus on converting numeric data types to strings and vice-versa.
"""


def calculate_profit():
    """
    Imagine this scenario: a company has determined that its annual profit is typically 23 percent of total sales.
    Complete this function so that it asks the user to enter in the projected amount of total sales and then displays the profit that will be made from that amount.
    You can assume the user will enter only numeric characters, e.g. "3000", not "$3,000.00"
    The output should match the format of the following examples: "Profit: $690.00" for sales of $3,000, or "Profit: $2,300.00" for sales of $10,000, etc.
    """
    total_sales=input("Please enter the projected amout of total sales. ")
    total_sales_as_int = int(total_sales)
    annual_profit = total_sales_as_int * 0.23
    annual_profit_as_int = int(annual_profit)
    print(f"Profit: ${annual_profit:.2f}")
    

def calculate_quotient_and_remainder():
    """
    Complete this function so that it asks the user to input two integers.
    You program should calculate and output the quotient and remainder when the first number is divided by the second.
    Here's an example run of the function:
      Enter number #1: 5
      Enter number #2: 2
      2 goes into 5 a total of 2 times with a remainder of 1
    """
    integer_1 = input("Please input your first integer. ")
    integer_2 = input("Please input your second integer. ")
    integer_1_as_int = int(integer_1)
    integer_2_as_int = int(integer_2)
    quotient = integer_1_as_int // integer_2_as_int
    remainder = integer_1_as_int % integer_2_as_int
    print(f"{integer_2_as_int} goes into {integer_1_as_int} a total of {quotient} times with a remainder of {remainder}")
def calculate_miles_per_gallon():
    """
    A car's Miles Per Gallon (MPG) can be calculated using the following formula:
      MPG = Miles driven / Gallons of Gas Used
    Complete this function so that it asks the user for the number of miles driven and the gallons of gas used.
    It should calculate the car's MPG and display the result in the format indicated in this example run of the program:

      Miles driven: 100
      Gas used (gallons): 25
      Miles per gallon: 2.2
    """
    Miles_driven = input("Please input the number of miles driven")
    Gallon_gas = input("Please input gallon of gas used")
    Miles_driven_as_int = int(Miles_driven)
    Gallon_gas_as_int = int(Gallon_gas)
    Miles_per_gallon = Miles_driven_as_int/Gallon_gas_as_int
    print("Miles driven:", Miles_driven)
    print("Gas used(gallons):", Gallon_gas)
    print("Miles per gallon:", Miles_per_gallon)
def align_text():
    """
    Complete this function such that it asks the user to enter in 3 price values (as floating point numbers).
    The print out the price values so that they are formatted to two decimal places. Also make sure that the price values are right aligned and line up at the decimal point.
    Here's a sample running of the program:

      Enter price #1: 1.55
      Enter price #2: 10
      Enter price #3: 9532.6

      Here are your prices!

      Price #1: $    1.55
      Price #2: $   10.00
      Price #3: $ 9532.60
    """
    Price_1 = float(input("Please enter price 1"))
    Price_2 = float(input("Please enter price 2"))
    Price_3 = float(input("Please enter price 3"))
    print("Here are your prices!")
    print("Price #1: $", format(Price_1, "8.2f"))
    print("Price #2: $", format(Price_2, "8.2f"))
    print("Price #3: $", format(Price_3, "8.2f"))
    