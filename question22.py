name=input("ENTER THE EMPLOYEES NAME")
salary=int(input("ENTER THE SALARY"))
year=int(input("ENTER THE YEAR OF SERVICE"))
if year>5:
	print("THE EMPLOYEE WILL GET NONUS OF 5% ")
	bonus=salary+salary*0.05
	print("SO THE BONUS IS ₹",bonus)
else:
	print("NO BONUS")