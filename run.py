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
        number_input = input('Enter measurement in meters (Eg 4.5):')

        try:
            val = float(number_input)
            return val
            break
        except ValueError:
            print("Error! Please input a measurement in meters e.g. 4.5")



def validate_int(data):
    """
    Validates if the value in the input is an int. 
    Used where a whole number is required for doors, windows and radiator inputs. 
    """

    while True:
        number_input = input('Enter number here (e.g. 3):')

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

def calculate_walls_area():
    """
    Calculates the cost of walls as per sizes input. 
    """

    length = room_length()
    width = room_width()
    height = room_height()

    walls_total_length = ((length + width) * 2) * 2
    walls_area = walls_total_length * height
    

    costs = []
    costs.append(sheet_data)
    for cost in costs:
        walls_rate = cost[1][1]

    total = walls_area * float(walls_rate)


    if float(walls_area) > 0:
        mats_cost = 55
    elif float(walls_area) > 50:
        mats_cost = 110
    elif float(walls_area) > 100:
        mats_cost = 165
    elif float(walls_area) > 150:
        mats_cost = 220

    total_walls_cost = total + mats_cost
    print(total_walls_cost)


def main():
    """
    Runs all functions
    """
    welcome()
    today()
    calculate_walls_area()

    

main()

