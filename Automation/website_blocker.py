import time
from datetime import datetime as dt

hosts_path = '/etc/hosts'

redirect = '127.0.0.1'

block_site_list = [
    'www.facebook.com', 'facebook.com', 'www.gmail.com', 'gmail.com', 'studio.youtube.com', 'www.youtube.com'
]

while 10 <= dt.now().hour <= 20:
    with open(hosts_path, 'r+') as file_ob:
        content = file_ob.read()
        for site in block_site_list:
            if not site in content:
                file_ob.write(redirect + " " + site + "\n")
else:
    with open(hosts_path, 'r+') as file_ob:
        content = file_ob.readlines()
        file_ob.seek(0)
        for line in content:
            if not any(site in line for site in block_site_list):
                file_ob.write(line)
        
        file_ob.truncate()

time.sleep(5)

# /home/gautham/Documents/CodingLabs/pybench/Automation/website_blocker.py