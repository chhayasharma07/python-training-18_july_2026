# 5. Insurance Premium Decision
# Take:
# •	customer age
# •	smoking habit
# •	BMI
# •	pre-existing disease status
# Rules:
# •	High premium for smokers with age > 50
# •	Medium premium for overweight users
# •	Reject if severe pre-existing disease and age > 60
# •	Low premium for healthy young users

age=int(input("Enter the customer age : "))
smoking=input("Do you smoke? (Yes/No) : ")
bmi=float(input("Enter the BMI : "))
disease=input("Do you have any pre-existing disease? (Yes/No) : ")

if disease.lower()=="yes" and age>60 :
    premium="Rejected"

elif smoking.lower()=="yes" and age>50 :
    premium="High Premium"

elif bmi>=25 :
    premium="Medium Premium"

else :
    premium="Low Premium"

print(f"Your insurance status is {premium}")