print("Input the price of 5 items from the store")

def Total_purchase():
    print("Thank you for shopping!")
item_1 = float(input("1st:"))
item_2 = float(input("2nd:"))
item_3 =float(input("3rd:"))
item_4 =float(input("4th:"))
item_5 =float(input("5th:"))

total = (item_1 + item_2 + item_3 + item_4 + item_5)

sales_tax = total*0.07

grand_total = total + sales_tax

print("subtotal:",total)
print("sales tax:",sales_tax)
print("grand total:",grand_total)

Total_purchase()
#Program #3, Donovan Thompson 1/29/25
