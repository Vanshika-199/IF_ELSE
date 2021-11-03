age1=int(input("enter the age"))
age2=int(input("enter the age"))
age3=int(input("enter the age"))
if age1<age2 and age1<age3:
	print("first person is youngest")
elif age2<age1 and age2<age3:
	print("second person is youngest")
else:
	print("third person is youngest")