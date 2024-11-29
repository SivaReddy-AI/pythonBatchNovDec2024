principal_amount = float(input("Enter the total pricipal amount :"))
rate_interst = float(input("Enter the rate of interst %:"))
time = float(input("Enter years:"))
simple_interst = principal_amount * rate_interst * time / 100
print(simple_interst)

n = int(input(" the number of times that interest is compounded per unit time :"))

compund_interst = principal_amount * (1 + rate_interst / n) ** n * time

print(compund_interst)
