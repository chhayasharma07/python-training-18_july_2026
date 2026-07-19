# 2. Loan Approval Engine
# Write a program to input:
# •	monthly salary
# •	credit score
# •	existing loan amount
# •	employment type
# Rules:
# •	Approve immediately if salary > 80000, credit score > 750, and existing loan < 20000
# •	Approve with caution if salary > 50000 and credit score > 650
# •	Reject if credit score < 600
# •	Else put under manual review

salary=int(input("Enter the monthly salary : "))
score=int(input("Enter the credit score : "))
loan=int(input("Enter the existing loan amount : "))
emp_type=input("Enter the employment type : ")

if salary>80000 and score>750 and loan<20000 :
    status="Approved"
    
elif salary>50000 and score>650 :
    status="Approved with caution"
    
elif score<600 :
    status="Reject"
    
else :
    status="Under manual review"
    
print(f"Your loan status is {status}")