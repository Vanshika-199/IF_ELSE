quantity=int(input("enter the quantity required"))
cost=100
purchase_amount=quantity*100
if purchase_amount>1000:
	discount=purchase_amount*0.1
	total=purchase_amount-discount
	print("you will get a discount of ₹",total)
else:
	print("NO DISCOUNT")