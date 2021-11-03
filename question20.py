unit=int(input("enter the unit comsumed by electricity    "))
if unit<=50:
	charge=unit*0.50
	fine=0
elif unit>=50 or unit<=100:
	charge=(unit*0.50)+((unit-50)*0.75)
	fine=0
elif unit>=100 or unit<=200:
	charge=(unit*0.50)+((unit-100)*1.20)
	fine=0
elif unit>=200 or unit<=250:
	charge=(unit*0.50)+((unit-200)*1.50)
	fine=charge*20/100
else:
	print("please visit the electric department")
	total=charge+fine
	print("total amount to be paid",total)