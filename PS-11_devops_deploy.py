# 10. DevOps Deployment Approval System
# Take:
# •	test coverage percentage
# •	security scan status
# •	code review status
# •	environment type
# Rules:
# •	Production deployment allowed only if all checks pass
# •	Staging may allow warning-based deployment
# •	Reject if security scan fails
# •	Conditional approval if review pending but environment is development

coverage=int(input("Enter the test coverage percentage : "))
security=input("Enter the security scan status (Pass/Fail) : ")
review=input("Enter the code review status (Pass/Pending) : ")
environment=input("Enter the environment type (Production/Staging/Development) : ")

if security.lower()=="fail" :
    status="Deployment Rejected"

elif environment.lower()=="production" and coverage>=80 and security.lower()=="pass" and review.lower()=="pass" :
    status="Deployment Approved"

elif environment.lower()=="staging" and coverage>=70 and security.lower()=="pass" :
    status="Deployment Approved with Warning"

elif environment.lower()=="development" and review.lower()=="pending" :
    status="Conditional Approval"

else :
    status="Deployment Rejected"

print(f"Deployment status is {status}")
