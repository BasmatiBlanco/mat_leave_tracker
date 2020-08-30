import datetime
from datetime import timedelta

employee = input("What is employee name ")
vacation_rate = int(input("Employee Vacation Entitlement "))
vacation_ytd = int(input("Used vacation days this year "))
ml_ed = ""
ml_sd = 0
leave_length = int(input("12 or 18 month leave? "))
due_date_entry = input("What is due date (YYYY-MM-DD)")
year, month, day = map(int, due_date_entry.split("-"))
due_date = datetime.date(year, month, day)

days = (5 * vacation_rate) - vacation_ytd
ml_sd = due_date_entry + timedelta(-days)
if leave_length == 12:
     days = 365
elif leave_length == 18:
    days = 548
ml_ed = due_date_entry + timedelta(+days) + timedelta(vacation_rate * 5)

print("This leave starts " + ml_sd)
print("this leave ends " + ml_ed)
