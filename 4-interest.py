principal=int(input("Enter the principal amount : "))
rate=float(input("Enter the rate of interest : "))
time=float(input("Enter the time period in years : "))

simple_interest=(principal*rate*time)/100

final_amount=principal*((1+(rate/100))**time)

compound_interest=final_amount-principal

print(f"The simple interest after {time} years is : {simple_interest}")

print(f"The compound interest after {time} years is : {compound_interest}")