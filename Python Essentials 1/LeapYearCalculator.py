year = int(input("Enter a year: "))

#
# Write your code here.
#	

year_is = "Not within the Gregorian calendar period"

if year >= 1582:
    if year % 4 != 0:
        year_is = "Common"
    elif year % 100 != 0:
        year_is = "Leap"
    elif year % 400 != 0:
        year_is = "Common"
    else: year_is = "Leap"

    print(f"{year} Is a {year_is} year")


print(f"{year} Is {year_is}")
