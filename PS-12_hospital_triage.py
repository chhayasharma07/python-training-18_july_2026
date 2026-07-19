# 11. Hospital Triage Priority System
# Input:
# •	patient age
# •	oxygen level
# •	heart rate
# •	symptom severity
# Rules:
# •	Oxygen below threshold → Emergency
# •	Elderly patient with severe symptoms → High priority
# •	Mild symptoms → General queue
# •	Else medium priority

age=int(input("Enter the patient age : "))
oxygen=int(input("Enter the oxygen level : "))
heart_rate=int(input("Enter the heart rate : "))
severity=input("Enter the symptom severity (Mild/Moderate/Severe) : ")

if oxygen<90 :
    priority="Emergency"

elif age>=60 and severity.lower()=="severe" :
    priority="High Priority"

elif severity.lower()=="mild" :
    priority="General Queue"

else :
    priority="Medium Priority"

print(f"Patient priority is {priority}")