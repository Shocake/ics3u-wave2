import string
month = string.capwords(input("Input a month"))
if month in ("April", "June", "September", "November"):
	print("30 days")
elif month in ("January", "March", "May", "July", "August", "October", "December"):
	print("31 days")
elif month == "February":
	print("28 or 29 days")