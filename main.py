appointment_lists = []

def add_record():

    is_valid_date()






def is_valid_date():

    date_input = input(print("What is the date Format (DD/MM/YYYY): "))
    day_string, month_string, year_string = date_input.split('/')

    year = int(year_string)
    month = int(month_string)
    day = int(day_string)
    if (2000 < year < 3000):
        return year
    else:
        print("This is a false year.")

    if (1 <= month <= 12):
        return month
    else:
        print("This is a false month")

    if (1 <= day <= daysInMonth(month,year)):
        return day

    else:
        print("This is a false day")

    print("year: " + year)
    print("month:" + month)
    print("day:" + day)




def daysInMonth(month, year,):

    #Leap Year
    if (year % 400 == 0 & year % 4 == 0 & year % 100 != 100):
        print("This is a leap year, There are 29 days in Feb")
        if (month == 2):
            return 29
        else:
            return
    elif(month == 1,3,5,7,8,10,12):
        return 31
    elif(month == 4,6,9,11):
        return 30
    elif(month == 2):
        return 28


def main():



    add_record()






if __name__ == "__main__":
    main()