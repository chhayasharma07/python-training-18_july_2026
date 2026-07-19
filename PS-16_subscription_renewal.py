# 15. Subscription Renewal Prediction
# Input:
# •	monthly usage
# •	missed payments
# •	support tickets count
# •	satisfaction score
# Rules:
# •	High usage + high satisfaction → Likely renew
# •	Low usage + many complaints → High churn risk
# •	Missed payments > threshold → Payment risk
# •	Else moderate renewal probability

usage=int(input("Enter the monthly usage : "))
payments=int(input("Enter the missed payments : "))
tickets=int(input("Enter the support tickets count : "))
score=int(input("Enter the satisfaction score : "))

if usage>80 and score>80 :
    status="Likely Renew"

elif usage<30 and tickets>5 :
    status="High Churn Risk"

elif payments>3 :
    status="Payment Risk"

else :
    status="Moderate Renewal Probability"

print(f"Subscription status is {status}")