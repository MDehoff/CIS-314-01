import re

log_entries = []
in_file = open("access.log")
in_data = in_file.readlines()

filter_entries = [entry for entry in log_entries if 'botpoke' not in entry]

remaining_count = len(filter_entries)
print(f"Number of remaining log entries: {remaining_count}")

ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
unique_ips = set()

for entry in filter_entries:
    match = ip_pattern.search(entry)
    if match:
        unique_ips.add(match.group())

print("Unique IP addresses:")
for ip in unique_ips:
    print(ip)
