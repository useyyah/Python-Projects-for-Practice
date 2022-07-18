import datetime

DAYS = ("Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday")
MONTHS = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

while True:
    response = input("Enter the year for the calendar: ")
    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
    print("Please enter a numeric year like 2022.")
    continue

while True:
    response = input("Enter the month for the calendar, 1-12: ")
    if not response.isdecimal():
        print("Please enter a numeric month.")
        continue
    month = int(response)
    if 1 <= month <= 12:
        break
    print("Please enter a number from 1 to 12.")


def get_calendar(year, month):
    cal_text = ""
    cal_text += (" " * 34) + MONTHS[month - 1] + " " + str(year) + "\n"
    cal_text += "...Sunday.....Monday....Tuesday...Wednesday...Thursday" \
                "....Friday....Saturday..\n"
    week_seperator = ("+----------" * 7) + "+\n"
    blank_row = ("|          " * 7) + "|\n"

    current_date = datetime.date(year, month, 1)
    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    while True:
        cal_text += week_seperator

        day_number_row = ""
        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += "|" + day_number_label + (" " * 8)
            current_date += datetime.timedelta(days=1)
        day_number_row += "|\n"

        cal_text += day_number_row
        for i in range(3):
            cal_text += blank_row
        if current_date.month != month:
            break
    cal_text += week_seperator
    return cal_text


cal_text = get_calendar(year, month)
print(cal_text)

calendar_filename = f"calendar_{year}_{month}.txt"
with open(calendar_filename, "w") as file_object:
    file_object.write(cal_text)
print(f"Saved to {calendar_filename}.")
