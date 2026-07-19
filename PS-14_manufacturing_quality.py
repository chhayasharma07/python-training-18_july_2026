# 13. Manufacturing Quality Check
# Input:
# •	defect count
# •	machine temperature
# •	production speed
# •	operator experience
# Rules:
# •	Reject batch if defects exceed limit
# •	If machine temperature is too high and speed is high → Risk
# •	If operator experience low and defect rising → Warning
# •	Else accept batch

defects=int(input("Enter the defect count : "))
temperature=int(input("Enter the machine temperature : "))
speed=int(input("Enter the production speed : "))
experience=int(input("Enter the operator experience (in years) : "))

if defects>50 :
    status="Batch Rejected"

elif temperature>90 and speed>100 :
    status="Risk"

elif experience<2 and defects>20 :
    status="Warning"

else :
    status="Batch Accepted"

print(f"Manufacturing status is {status}")