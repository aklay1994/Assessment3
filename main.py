appointment_lists = []

def add_record():


    #Ask for Date and validate the date.
    date_input = input(print("What is the date Format (DD/MM/YYYY): "))
    is_valid_date(date_input)

    #Ask for start and end time and validate
    start_time_input = input("What is the start-time (8-21): ")
    end_time_input = input("What is the end-time(8-21): ")
    is_valid_time(start_time_input, end_time_input)








def is_valid_date(date_input):

    string_parts = date_input.split('/')

    if len(string_parts != 3 ):
        print("Error, Date must be in format (DD/MM/YYYY)")
        return False

    day_string, month_string, year_string = string_parts

    if not (day_string and month_string and year_string):
        print("Error, Day and month and year must be provided")
        return False

    if not (day_string.isdigit() and month_string.isdigit() and year_string.isdigit()):
        print("Error. Date parts must be digits")
        return False

    if (len(day_string) > 1 and day_string[0] == '0') or (len(month_string) > 1 and month_string[0] == '0'):
        print("Error. Date parts must not lead with zeros")
        return False

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

    is_valid_time()



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



def is_valid_time(start_time_input, end_time_input):

    try:
        start = int(start_time_input)
        end = int(end_time_input)
    except ValueError:
        print("Error: Use integers for time.")
        return False


    if (start_time_input < 8 or start_time_input > 21):
        print("Invalid Start-time.")
        return False

    if(end_time_input < 8 or end_time_input > 21):
        print("Invalid end-time.")
        return False

    if (start >= end):
        print("Start-time must be before the End-Time.")
        return False

    return True



def is_concurrent_appointment(new_user_date, new_user_start,new_user_end):
    for appointment in appointment_lists:

        time_parts = appointment.split(';')
        if (len(time_parts) != 4):
            continue


        date, subject, start_string, end_string = time_parts

        try:
            start = int(start_string)
            end = int(end_string)

        except ValueError:
            continue


        if date == new_user_date:

            if (new_user_start < end) and (start < new_user_end):
                print(f"Error: conflicting with existing appointment: {subject} ({start}-{end})")
                return True

    return False

def main():



    add_record()






if __name__ == "__main__":
    main()