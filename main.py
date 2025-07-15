appointment_lists = []

def add_record():

    is_valid_date()






def is_valid_date():

    date_input = input(print("What is the date Format (DD/MM/YYYY): "))
    day_string, month_string, year_string = date_input.split('/')

    year = int(year_string)
    month = int(month_string)
    day = int(day_string)

    if (year < 2025 or year > 3000):
        print("Invalid Year")
        return False

    if (month <1 or month > 12):
        print("Invalid Month")
        return False

    if (1<= day <= daysInMonth(month, year)):
        print("This is a valid Day")
    else:
        print("This is not a valid day")



def daysInMonth(month, year,):

    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("This is a leap year, therefore 28 days in Feb.")
            return 29
        else:
            return 28




def main():



    add_record()






if __name__ == "__main__":
    main()