name=input("enter the name of the student")
class_held=int(input("enter no.of classess held"))
class_attend=int(input("enter class attended"))
percentage=class_attend/class_held*100
if percentage>=75:
	print("have a good percentage and the student is allowed to sit in the exam")
else:
	print("the percentage is very low abd the student is not allowed to give the exam'")