a=float(input("Marks of physics"))
b=float(input("Marks of chemistry"))
c=float(input("Marks of biology"))
d=float(input("Marks of mathematics"))
e=float(input("Marks of computer"))
attained_marks=a+b+c+d+e
total=1000
percentage=attained_marks/total*100
if percentage>=90:
	print("Grade A")
if percentage>=80:
	print("Grade B")
elif percentage>=70:
	print("Grade C")
elif percentage>=60:
	print("Grade D")
elif percentage>=50:
	print("Grade E")
elif percentage<40:
	print("Grade F")
else:
	print("Not defined")