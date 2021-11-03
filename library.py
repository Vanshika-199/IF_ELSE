ex_day=int(input('enter the returning day'))
ex_month=int(input('enter the returning month'))
ex_year=int(input('enter the returning year'))
act_day=int(input('enter the actual returning day'))
act_month=int(input('enter the actual returning month'))
act_year=int(input('enter the actual returning year'))
if ex_day<=act_day:
	if ex_month==act_month:
		if ex_year==act_year:
			print("no charges")
if ex_day>act_day:
	if ex_month==act_month:
		if ex_year==act_year:
			late = ex_day-act_day
			fine=15*late
			print("₹ 15 for one day, so the fine is ₹",fine)
if ex_day>act_day:
	if ex_month>act_month:
		if ex_year==act_year:
			late=(ex_day-act_day)+(ex_month-act_month)
			fine=500*late
			print("₹ 500 for one day, so the fine is ₹",fine)
if ex_day>act_day:
	if ex_month>act_month:
		if ex_year>act_year:
			fine=10000
			print("₹",fine,"is fixed")