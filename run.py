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
costs = []
costs.append(sheet_data)

estimate = SHEET.worksheet('estimate')


def welcome():
    """
    Welcome information and input for relevant customer name for the job being estimated.
    """
    print("Welcome to the Room Decorating Cost Estimator.")
    print("Please input the required information when prompted.")
    print()
    
    global cust_name
    cust_name = input("Enter customer name here:\n")

    name_cell = estimate.cell(4, 1).value
    estimate.update_cell(4, 1, cust_name)
    

def today():
    """
    Automatically inputs the date of estimate creation"
    """
    print()
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
    Ensures that inputs are floats.
    """

    measurement = validate_float(data)
    return measurement

def number(data):
    """
    Validates measurement inputs from room_length, room_width and room_height functions.
    Ensures that inputs are integers.
    """
    number = validate_int(data)
    return number


def room_length():
    """
    Takes user input for room length
    """

    print('Room Length:')
    global length
    length = measurement(measurement)
    print()
    return length

def room_width():
    """
    Takes user input for room width
    """

    print('Room Width:')
    global width
    width = measurement(measurement)
    print()
    return width

def room_height():
    """
    Takes user input for room height
    """

    print('Room Height:')
    global height
    height = measurement(measurement)
    print()
    return height

def calculate_walls_area(num1, num2, num3):
    """
    Works out total wall area for 2 coats of paint.
    Calculates the labour cost of walls as per sizes input. 
    Calculates the amount of paint needed and cost.
    Totals labour and paint to a final figure.
    Asks user if it is a kitchen or bathrooms and adjusts the overall walls price * 1.5 to allow for
    extra time when painting complex rooms and an increase in the cost of appropriate paint. 
    """

    walls_total_length = ((num1 + num2) * 2) * 2
    walls_area = walls_total_length * num3
    
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
    global total_walls_cost
    total_walls_cost = round(total_walls, 2)

    room_type_input = input("Is the room a Kitchen or Bathroom? yes/no:\n")

    if room_type_input == "yes":
        total_walls_cost = total_walls_cost * 1.5
        return total_walls_cost
    else:
        return total_walls_cost


def calculate_skirtings():
    """
    Takes the room dimensions, adds them and doubles them to give us the total
    metergae of skirting boards.
    Uses the rate fromn the spreadsheet to return the total cost. 
    """
    print()
    skirtings_length = (length + width) * 2
    print(f"There are {skirtings_length}m of skirting boards.")
    for cost in costs:
        skirtings_rate = cost[1][4]

    global skirtings_total_cost
    skirtings_total_cost = skirtings_length * float(skirtings_rate)
    return skirtings_total_cost

def calculate_ceilings(num1, num2):
    """
    Calculates area of ceiling and determines the cost using the
    predetermined rate per m2 for labour and materials from the spreadsheet.
    """
    ceiling_area = (num1 * num2) * 2

    for cost in costs:
        ceiling_rate = cost[1][1]
    
    total_ceiling = ceiling_area * float(ceiling_rate)
    global total_ceiling_cost
    total_ceiling_cost = round(total_ceiling, 2)
    return total_ceiling_cost


def calculate_doors():
    """
    Calculates the cost for all doors using the rate from the spreadsheet.
    Takes a user input for the qty of doors in the room.
    """
    print()
    print("Enter number of doors:")
    doors = validate_int(number)
    for cost in costs:
        doors_rate = cost[1][2]
    
    global doors_total_cost
    doors_total_cost = int(doors) * float(doors_rate)
    return doors_total_cost
    


def calculate_windows():
    """
    Calculates the cost for all windows using the rate from the spreadsheet.
    Takes a user input for the qty of windows in the room.
    """
    print()
    print("Enter number of windows:")
    windows = validate_int(number)
    for cost in costs:
        windows_rate = cost[1][3]
    
    global windows_total_cost
    windows_total_cost = int(windows) * float(windows_rate)
    return windows_total_cost
    

def calculate_radiators():
    """"
    Takes user input for number of radiators in the room if they are to be apinted. 
    Uses rate from spreadsheet and totals the cost.
    """
    print()
    print("Enter number of radiators:")
    radiators = validate_int(number)
    for cost in costs:
        radiators_rate = cost[1][5]
    
    global radiators_total_cost

    radiators_total_cost = int(radiators) * float(radiators_rate)
    return radiators_total_cost
    

def total_estimate(num1, num2, num3, num4, num5, num6):
    """
    Adds all of the costs together and returns the final estimate.
    """
    print()
    global total_price
    total_price = num1 + num2 + num3 + num4 + num5 + num6
    total_price = round(total_price, 2)
    print(f"Total Estimate is:\n£{total_price}")
    return total_price


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
    calculate_skirtings()
    calculate_ceilings(length, width)
    calculate_doors()
    calculate_windows()
    calculate_radiators()
    total_estimate(total_walls_cost, total_ceiling_cost, doors_total_cost, windows_total_cost, skirtings_total_cost, radiators_total_cost)
    

main()

