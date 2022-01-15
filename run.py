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

data = costs.get_all_values()


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

welcome()

def today():
    """
    Automatically inputs the date of estimate creation"
    """
    today = date.today()
    print("Date of estimate:")
    print(today)
    return today

today()


