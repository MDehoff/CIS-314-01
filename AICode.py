import re

def extract_unique_ips(log_file):
    # Regular expression pattern to match IP addresses
    ip_pattern = r'(?<!\d)(?:\d{1,3}\.){3}\d{1,3}(?!\d)'
    
    unique_ips = set()  # Use a set to store unique IP addresses
    
    with open(log_file, 'r') as file:
        for line in file:
            # Find all IP addresses in the line
            ips = re.findall(ip_pattern, line)
            # Add found IPs to the set
            unique_ips.update(ips)
    
    return unique_ips

# Example usage
log_file_path = 'webserver.log'  # Replace with your log file path
unique_ips = extract_unique_ips(log_file_path)

print("Unique IP Addresses:")
for ip in unique_ips:
    print(ip)
