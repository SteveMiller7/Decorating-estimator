import gspread
from google.oauth2.service_account import Credentials
from datetime import date

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('decorating_estimator')

costs = SHEET.worksheet('costs')

sheet_data = costs.get_all_values()


def welcome():
    """
    Welcome information and input for relevant customer name for the job being estimated.
    """
    print("Welcome to the Room Decorating Cost Estimator.")
    print("Please input the required information when prompted.")
    print()
    cust_name = input('Enter customer name here:\n')
    print()
    return cust_name
    Print()


def today():
    """
    Automatically inputs the date of estimate creation"
    """
    today = date.today()
    print("Date of estimate:")
    print(today)
    print()
    return today


def validate_float(data):
    """
    Validates if the value in the input is a float. 
    Used where a meterage measurement is required. 
    """

    while True:
        number_input = input('Enter measurement in meters (eg 2.5):\n')

        try:
            val = float(number_input)
            return val
            break
        except ValueError:
            print("Error! Please input a measurement in meters e.g. 2.5")



def validate_int(data):
    """
    Validates if the value in the input is an int. 
    Used where a whole number is required for doors, windows and radiator inputs. 
    """

    while True:
        number_input = input()

        try:
            val = int(number_input)
            return val
            break
        except ValueError:
            print("Error! Please input a whole number!")


def measurement(data):
    """
    Validates measurement inputs from room_length, room_width and room_height functions.
    Ensures that inputs are integers.
    """

    measurement = validate_float(data)
    return measurement


def room_length():
    """
    Takes user input for room length
    """

    print('Room Length:\n')
    length = measurement(measurement)
    print()
    return length

def room_width():
    """
    Takes user input for room width
    """

    print('Room Width:\n')
    width = measurement(measurement)
    print()
    return width

def room_height():
    """
    Takes user input for room height
    """

    print('Room Height:\n')
    height = measurement(measurement)
    print()
    return height

def calculate_walls_area(num1, num2, num3):
    """
    Works out total wall area for 2 coats of paint.
    Calculates the labour cost of walls as per sizes input. 
    Calculates the amount of paint needed and cost.
    Totals labour and paint to a final figure.
    """

    walls_total_length = ((num1 + num2) * 2) * 2
    walls_area = walls_total_length * num3
    

    costs = []
    costs.append(sheet_data)
    for cost in costs:
        walls_rate = cost[1][0]

    total = walls_area * float(walls_rate)


    if float(walls_area) > 0:
        mats_cost = 55
    elif float(walls_area) > 50:
        mats_cost = 110
    elif float(walls_area) > 100:
        mats_cost = 165
    elif float(walls_area) > 150:
        mats_cost = 220

    total_walls = total + mats_cost
    total_walls_cost = round(total_walls, 2)
    print(total_walls_cost)
    return total_walls_cost

def calculate_ceilings(num1, num2):
    """
    Calculates area of ceiling and determines the cost using the
    predetermined rate per m2 for labour and materials from the spreadsheet.
    """
    ceiling_area = (num1 * num2) * 2

    costs = []
    costs.append(sheet_data)
    for cost in costs:
        ceiling_rate = cost[1][1]
    
    total_ceiling = ceiling_area * float(ceiling_rate)
    total_ceiling_cost = round(total_ceiling, 2)
    print(total_ceiling_cost)
    print()

def calculate_doors():

    doors_input = input('Enter number of doors:\n')

    costs = []
    costs.append(sheet_data)
    for cost in costs:
        ceiling_rate = cost[1][2]
    

    doors_total_cost = int(doors_input) * float(ceiling_rate)
    print(doors_total_cost)


def main():
    """
    Runs all functions
    """
    welcome()
    today()
    length = room_length()
    width = room_width()
    height = room_height()
    calculate_walls_area(length, width, height)
    calculate_ceilings(length, width)
    calculate_doors()
    

main()

