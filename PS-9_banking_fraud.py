# 8. Banking Fraud Detection Logic
# Take:
# •	transaction amount
# •	location mismatch
# •	unusual login time
# •	account age
# Rules:
# •	High-value transaction with location mismatch → Fraud alert
# •	New account with unusual login time → Risk alert
# •	Medium transaction but repeated unusual activity → Review
# •	Else approve transaction

amount=int(input("Enter the transaction amount : "))
location=input("Is there a location mismatch? (Yes/No) : ")
login=input("Is the login time unusual? (Yes/No) : ")
age=int(input("Enter the account age (in months) : "))

if amount>100000 and location.lower()=="yes" :
    status="Fraud Alert"

elif age<6 and login.lower()=="yes" :
    status="Risk Alert"

elif amount>50000 and login.lower()=="yes" :
    status="Review"

else :
    status="Approved"

print(f"Transaction status is {status}")