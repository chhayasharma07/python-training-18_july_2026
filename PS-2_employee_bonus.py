# 1. Employee Performance Bonus System
# Create a program that takes:
# •	employee rating
# •	years of experience
# •	project delivery status
# Rules:
# •	If rating is 5, experience > 10, and project delivery is "on time", give 30% bonus
# •	If rating is 4 and experience > 7, give 20% bonus
# •	If rating is 3 and project delivery is "delayed", give 5% bonus
# •	Otherwise, no bonus

emp_rating=int(input("Enter the employee rating : "))
year=int(input("Enter the years of experience : "))
status=input("Enter the delievery status : ")

if emp_rating==5 and year>10 and status=="on time" :
    bonus="30%"
    
elif emp_rating==4 and year>7 :
    bonus="20%"
    
elif emp_rating==3 and status=="delayed" :
    bonus="5%"
    
else :
    bonus="no"
    
print(f"The bonus is = {bonus}")