# Problem Statement: Employee Loan Eligibility System Using if-elif-else
# A bank wants to create a Python application to check whether a working professional is eligible for a personal loan.

# The loan decision will be based on:
# •	Applicant’s age 
# •	Monthly salary 
# •	Total work experience 
# •	Credit score 
# •	Existing monthly EMI 

# Eligibility Rules
# 1.	The applicant’s age must be between 21 and 58 years. 
# 2.	The applicant must have at least 2 years of work experience. 
# 3.	The applicant’s credit score must be at least 650. 
# 4.	Loan eligibility will be decided using the following salary rules: 

# Monthly Salary	    Maximum Loan Eligibility
# ₹25,000–₹39,999	    ₹2,00,000
# ₹40,000–₹59,999	    ₹5,00,000
# ₹60,000–₹99,999	    ₹10,00,000
# ₹1,00,000 or above	₹15,00,000

# 5.	The existing EMI should not be more than 40% of the monthly salary. 
# 6.	When any mandatory condition is not satisfied, the application should be rejected with an appropriate reason. 

# Expected Input
# Enter applicant name:
# Enter age:
# Enter monthly salary:
# Enter work experience in years:
# Enter credit score:
# Enter existing monthly EMI:

# Expected Output Example
# Applicant Name: Rahul Sharma
# Loan Application Status: Eligible
# Maximum Loan Amount: ₹5,00,000
# Or:
# Applicant Name: Rahul Sharma
# Loan Application Status: Rejected
# Reason: Credit score is below 650.

name=input("Enter the name : ")
age=int(input("Enter the age : "))
salary=int(input("Enter the monthly salary : "))
exp=int(input("Enter total work experience in years : "))
score=int(input("Enter your credit score : "))
emi=int(input("Enter the existing EMI : "))


if age>=21 and age<=58 :
    if exp>=2:
        if score>=650:
            if emi<=(40*salary)/100:
               if salary>=25000 and salary<=39999:
                loan="elegible"
                amount=200000
                
               elif salary>=40000 and salary<=59999:
                loan="elegible"
                amount=500000
                
               elif salary>=60000 and salary<=99999:
                loan="elegible"
                amount=1000000
                
               elif salary>=100000 :
                loan="elegible"
                amount=1500000
                
            else:
              loan="Rejected"
              reason="EMI is more than 40 percent of the monthly salary"
                
        else:
            loan="Rejected"
            reason="Credit Score is below 650"
    
    else:
        loan="Rejected"
        reason="Exp is less than 2 years"
        
else:
    loan="Rejected"
    reason="Age is not elegible"
    
if(loan == "elegible"):
    print(f"Name : {name} Status: {loan} value : {amount}")
    
else:
    print(f"Name : {name} Status: {loan} reason : {reason}")
        