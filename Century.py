year_to_check = int(input("please type in the year: "))
def centuryFromYear(year):
    return (year - 1) // 100 + 1
print(centuryFromYear(year_to_check))