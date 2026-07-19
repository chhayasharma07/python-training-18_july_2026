# 7. Server Health Monitoring Decision
# Input:
# •	CPU usage
# •	memory usage
# •	disk usage
# •	network latency
# Rules:
# •	If CPU > 90 and memory > 85 → Critical alert
# •	If disk > 95 → Storage critical
# •	If latency > threshold → Network issue
# •	Else classify as healthy / warning / critical

cpu=int(input("Enter the CPU usage (%) : "))
memory=int(input("Enter the memory usage (%) : "))
disk=int(input("Enter the disk usage (%) : "))
latency=int(input("Enter the network latency (ms) : "))

if cpu>90 and memory>85 :
    status="Critical Alert"

elif disk>95 :
    status="Storage Critical"

elif latency>100 :
    status="Network Issue"

elif cpu>70 or memory>70 or disk>80 :
    status="Warning"

else :
    status="Healthy"

print(f"Server status is {status}")