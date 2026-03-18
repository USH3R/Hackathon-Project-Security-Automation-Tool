import os

# A simple tool to format suspicious IPs for a blocklist
def add_to_blocklist(ip_address):
    with open("blocklist.txt", "a") as file:
        file.write(ip_address + "\n")
    print(f"Successfully automated: {ip_address} added to blocklist.")

# Test the tool
target_ip = input("Enter suspicious IP: ")
add_to_blocklist(target_ip)
