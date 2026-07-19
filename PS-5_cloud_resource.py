# 4. Cloud Resource Billing System
# Input:
# •	number of compute hours
# •	storage used
# •	support plan type
# Rules:
# •	Basic plan: fixed support fee
# •	Premium plan: higher support fee but discounted compute
# •	Enterprise plan: custom rate with storage discount
# •	Final bill depends on multiple slabs


hours=int(input("Enter the compute hours : "))
storage=int(input("Enter the storage used (GB) : "))
plan=input("Enter the support plan (Basic/Premium/Enterprise) : ")

if plan.lower()=="basic" :
    support_fee=500
    compute_rate=10
    storage_rate=2

elif plan.lower()=="premium" :
    support_fee=1000
    compute_rate=8
    storage_rate=2

elif plan.lower()=="enterprise" :
    support_fee=2000
    compute_rate=6
    storage_rate=1

else :
    support_fee=0
    compute_rate=10
    storage_rate=2

compute_bill=hours*compute_rate
storage_bill=storage*storage_rate
bill=compute_bill+storage_bill+support_fee

if bill<=5000 :
    final_bill=bill

elif bill<=10000 :
    final_bill=bill-(bill*0.05)

else :
    final_bill=bill-(bill*0.10)

print(f"Your final bill is {final_bill}")