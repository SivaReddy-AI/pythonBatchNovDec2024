pricepal_amount = float(input("Enter the pricepal amount "))
rate_of_interst = float(input("Enter rate of interst % :"))
number_years = float(input("Enter the number of years :"))
number_of_years_compound = int(input("Enter the number of times compound is cal:"))
simple_interst = pricepal_amount * rate_of_interst * number_years /100
print(simple_interst)
compund_interst = pricepal_amount * (1+ rate_of_interst /number_of_years_compound) ** number_of_years_compound * number_years
print("Your total compound_interst is" ,compund_interst )
