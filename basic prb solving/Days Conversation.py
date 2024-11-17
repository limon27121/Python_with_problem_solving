Days=int(input("enter Days:"))

year=int(Days/365)
week=(Days-year*365)%7
days=Days-(year*365+week*7)


print(year)
print(week)
print(days)
