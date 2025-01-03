"""While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 1000. 
If quantity and price per item are input through the keyboard, write a program to calculate the  total  expenses."""

#discount=10%



quantity=int(input("Enter the quantity:--"))
price=int(input("Enter the price of per item :--"))

total_price=quantity*price

print(total_price)

discount=10/total_price

print(discount)
