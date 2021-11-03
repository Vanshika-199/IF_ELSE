Atm question

lang=int(input('enter the language  '))
if lang==1:
	print('hindi')
elif lang==2:
	print('english')
else:
	print('please choose a language  ')
print('welcome to punjab national bank')
user_pin=4623
user_pin=int(input('enter the pin  '))
if user_pin==4623:
	print('correct pin')
else:
	print('incorrect pin')
balance=5000
if user_pin==4623:
	choose=int(input('PLEASE CHOOSE AN OPTION FROM THE FOLLOWING 1. withdraw 2.balance enquiry 3.deposit   '))
	if choose==1:
		print("withdraw")
		withdraw=int(input('enter the withdraw amount  '))
		if withdraw<balance:
			balance=balance
			print('withdraw amount is',withdraw,'and the remaining balance is',balance)
		else:
			print('INSUFFICIENT BALANCE')
	elif choose==2:
		print("balance")
		balance=balance-withdraw
		print("the balance in your account is",balance)
	elif choose==3:
		print("deposit")
		deposit=int(input('enter the deposit amount  '))
		deposit=balance+deposit
		print('so now the total balance is',deposit)
	else:
		print('INSUFFICIENT BALANCE')
else:
	print('wrong pin')
print('THANK YOU FOR VISITING')