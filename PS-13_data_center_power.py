# 12. Data Center Power Usage Classification
# Take:
# •	total power consumption
# •	cooling efficiency
# •	rack load percentage
# Rules:
# •	If power exceeds safe limit and cooling is poor → Critical
# •	If rack load > threshold → Warning
# •	Efficient cooling and balanced load → Normal
# •	Else moderate risk

power=int(input("Enter the total power consumption : "))
cooling=input("Enter the cooling efficiency (Good/Poor) : ")
rack=int(input("Enter the rack load percentage : "))

if power>1000 and cooling.lower()=="poor" :
    status="Critical"

elif rack>80 :
    status="Warning"

elif cooling.lower()=="good" and rack<=80 :
    status="Normal"

else :
    status="Moderate Risk"

print(f"Data center status is {status}")