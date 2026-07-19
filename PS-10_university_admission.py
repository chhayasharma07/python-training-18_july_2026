# 9. University Admission Eligibility
# Input:
# •	entrance exam score
# •	12th percentage
# •	category
# •	extracurricular score
# Rules:
# •	High score + strong academics → Direct admission
# •	Reserved category may have relaxation
# •	Moderate score + extracurricular achievements → Waitlist
# •	Low score → Reject

exam=int(input("Enter the entrance exam score : "))
percentage=float(input("Enter the 12th percentage : "))
category=input("Enter the category (General/Reserved) : ")
extra=int(input("Enter the extracurricular score : "))

if exam>=90 and percentage>=85 :
    status="Direct Admission"

elif category.lower()=="reserved" and exam>=80 and percentage>=75 :
    status="Direct Admission"

elif exam>=70 and extra>=80 :
    status="Waitlist"

else :
    status="Reject"

print(f"Admission status is {status}")