# 14. IT Helpdesk Ticket Prioritization
# Take:
# •	issue severity
# •	department
# •	business impact
# •	VIP user status
# Rules:
# •	Critical severity + VIP user → P1
# •	Critical severity + high business impact → P1
# •	Medium severity → P3
# •	Low severity → P4
# •	Else assign appropriate priority

severity=input("Enter the issue severity (Critical/Medium/Low) : ")
department=input("Enter the department : ")
impact=input("Enter the business impact (High/Medium/Low) : ")
vip=input("Is the user a VIP? (Yes/No) : ")

if severity.lower()=="critical" and vip.lower()=="yes" :
    priority="P1"

elif severity.lower()=="critical" and impact.lower()=="high" :
    priority="P1"

elif severity.lower()=="medium" :
    priority="P3"

elif severity.lower()=="low" :
    priority="P4"

else :
    priority="P2"

print(f"Ticket priority is {priority}")