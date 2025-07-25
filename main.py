appointment_lists = []

def leap_year(year):
    if (year % 400 == 0):
        return True
    if (year % 100 == 0):
        return False
    if (year % 4 == 0):
        return True
    return False


def check_date(date):
    try:
        day, month, year = date.split("/")
        day = int(day)
        month = int(month)
        year = int(year)
    except:
        print("Use format DD/MM/YYYY")
        return False

    if (year <2025 or year > 3000):
        print("Year must be between 2025 and 2999")
        return False
    if (month < 1 or month >12):
        print("Month must be between 1 and 12")
        return False

    if month in [4,6,9,11] and day > 30:
        print("This month only has 30 days")
        return False
    elif (month == 2):
        if leap_year(year) and day > 29:
            print("February only has 29 day in leap years")
            return False
        elif not (leap_year(year) and day > 28):
            print("February only has 28 days this year")
            return False
    elif day > 31:
        print("This month only has 31 days")
        return False
    if day < 1:
        print("Day must be greater than 1")
        return False

    return True

def check_time(start, end):
    try:
        start = int(start)
        end = int(end)
    except:
        print("Please enter Whole numbers.")
        return False

    if (start < 8 or end > 21):
        print("Appointments must be between 8am and 9pm")
        return False

    if (start >= end):
        print("End time must be after start time")
        return False
    return True



def is_concurrent_appointment(date, start, end):
    for app in appointment_lists:
        app_date, app_subject, app_start, app_end = app.split(";")
        if (app_date == date):
            app_start = int(app_start)
            app_end = int(app_end)

            if not (end <= app_start or start >= app_end):
                print(f"Overlaps with: {app_subject} ({app_start}-{app_end})")
                return True
    return False



def add_record():
    print("\nAdd new Appointment")

    while True:
        date = input(print("Enter a date (DD/MM/YYYY or EXIT): ")).strip()
        if date.upper() == "EXIT":
            break

        if not check_date(date):
            continue

        subject = input(print("Subject (1-32 Characters): ")).strip()
        if len(subject) == 0 or len(subject) > 32:
            print("Subject must be 1-32 characters")
            continue

        start = input(print("Start Time (8-21): ")).strip()
        end = input(print("End Time (8-21): ")).strip()

        if not check_time(start, end):
            continue
        if is_concurrent_appointment(date, int(start), int(end)):
            print("Can't add overlapping appointment")
            continue

        appointment_lists.append(f"{date}; {subject};{start};{end}")
        print("Appointment Added")
        break

def show_records():
    print("\nAll Appointments")

    if not appointment_lists:
        print("No Appointments Made Yet")
        return

    print("Date       | Subject              | Start | End")
    print("----------------------------------------------")

    for app in appointment_lists:
        date, subject, start_time, end_time = app.split(";")
        print(f"{date:<10} | {subject:<20} | {start_time:>5} | {end_time:>3}")


def sort_records():
    if not appointment_lists:
        print("No appointments to sort.")
        return


    while True:
        user_choice = input(print("\nSort Appointments by time? (YES/EXIT): ")).strip().upper()
        if user_choice == "EXIT":
            return
        if user_choice == "YES":
            break
        print("Only Enter YES or EXIT.")

        n = len(appointment_lists)
        for i in range(n):
            for j in range(0, n-i-1):

                date1 = appointment_lists[j].split(";")[0]
                date2 = appointment_lists[j+1].split(";")[0]
                day1, month1, year1 = map(int, date1.split("/"))
                day2, month2, year2 = map(int, date2.split("/"))

                if (year1 > year2):
                    appointment_lists[j], appointment_lists[j+1] = appointment_lists[j+1], appointment_lists[j]
                elif(year1 == year2):
                    if (month1 > month2):
                        appointment_lists[j], appointment_lists[j + 1] = appointment_lists[j + 1], appointment_lists[j]
                    elif (month1 == month2):
                        if (day1 > day2):
                            appointment_lists[j], appointment_lists[j + 1] = appointment_lists[j + 1], appointment_lists[j]
                        elif (day1 == day2):

                            t1 = int(appointment_lists[j].split(";")[2])
                            t2 = int(appointment_lists[j+1].split(";")[2])

                            if (t1 > t2):
                                appointment_lists[j], appointment_lists[j + 1] = appointment_lists[j + 1], appointment_lists[j]


    print("Appointments Sorted!!")
    show_records()


#===========================Main Program============================#
def main():

        print("Simple Program Scheduler")

        while True:
            print("\nMenu")
            print("1. Add Appointment")
            print("2. View Appointments")
            print("3. Sort Appointments")
            print("4. Quit")


            user_choice = input(print("Enter Your Choice (1-4): "))

            if user_choice == "1":
                add_record()
            elif user_choice == "2":
                show_records()
            elif user_choice == "3":
                sort_records()
            elif user_choice == "4":
                print("Exiting Program")
            else:
                print("Please enter (1-4).")


if __name__ == "__main__":
    main()