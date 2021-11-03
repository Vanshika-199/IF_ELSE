a=float(input("enter the first side"))
b=float(input("enter the second side"))
c=float( input("enter the third side"))
if a+b>c or a+c>b or b+c>a:
	print("triangle is valid")
else:
	print("triangle is not valid")