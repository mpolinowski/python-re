import re

ip_file = 'ip.txt'

# extract specific IPs from file

with open(ip_file, 'r') as file:
    file_content = file.read()
    # print(file_content)

ip_pattern = re.compile("[0-9]{3}\.[0-9]{3}\.2\.[0-9]{3}")
ip_matches = ip_pattern.findall(file_content)
print(ip_matches) 
