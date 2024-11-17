from datetime import datetime,timedelta

# Get the current date and time
# today = datetime.now()

# print("Current date and time:", today)

# oneday=timedelta(days=1)
# yesterday=today-oneday
# print(type(str(yesterday)))

# print(today.day)
# print(type(today.month))
# print(today.year)

birthday=input("enter your birthday (dd/mm/yyyy)")

print(type(birthday))


# convert it from string to date-time

birthdate=datetime.strptime(birthday,'%d/%m/%Y')

print(str(birthdate))

oneday=timedelta(days=1)
birthday_env=birthdate-oneday
print(birthday_env.day)