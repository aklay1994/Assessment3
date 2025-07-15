appointment_lists = []

def add_record():






def is_valid_date():

    date_input = input(print("What is the date Format (DD/MM/YYYY): "))
    day_string, month_string, year_string = date_input.split('/')




def daysInMonth(month, year,):

    #Leap Year
    if (year % 400 == 0 & year % 4 == 0):
        print("This is a leap year, There are 29 days in Feb")
        if (month == 2):
            print("There are 29 days in this month?")
