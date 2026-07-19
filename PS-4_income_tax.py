# 3. Income Tax Calculator
# Create a tax calculation system based on:
# •	annual income
# •	age
# •	investment amount
# Sample logic:
# •	If age >= 60, allow senior citizen exemption
# •	If income < 500000, tax = 0
# •	If income between 500000 and 1000000, tax = 10%
# •	If income between 1000000 and 2000000, tax = 20%
# •	Above that, tax = 30%
# •	Deduct exemptions based on investments


income=int(input("Enter the annual income : "))
age=int(input("Enter the age : "))
investment=int(input("Enter the investment amount : "))

if age>=60 :
    exemption=50000

else :
    exemption=0

if income<500000 :
    tax=0

elif income<=1000000 :
    tax=income*0.10

elif income<=2000000 :
    tax=income*0.20

else :
    tax=income*0.30

tax=tax-investment-exemption

if tax<0 :
    tax=0

print(f"Your income tax is {tax}")