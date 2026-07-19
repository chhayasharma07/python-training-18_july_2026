# 6. E-commerce Discount and Shipping Engine
# Input:
# •	cart value
# •	customer type
# •	coupon code
# •	membership status
# Rules:
# •	Premium members get free shipping
# •	Cart above ₹5000 gets 20% discount
# •	Cart above ₹2000 gets 10% discount
# •	Coupon applies only if valid
# •	Final payable amount should be displayed

cart=int(input("Enter the cart value : "))
customer=input("Enter the customer type : ")
coupon=input("Enter the coupon code : ")
membership=input("Enter the membership status (Premium/Regular) : ")

if membership.lower()=="premium" :
    shipping=0

else :
    shipping=100

if cart>5000 :
    discount=cart*0.20

elif cart>2000 :
    discount=cart*0.10

else :
    discount=0

if coupon=="SAVE100" :
    coupon_discount=100

else :
    coupon_discount=0

final_amount=cart-discount-coupon_discount+shipping

print(f"Your final payable amount is {final_amount}")