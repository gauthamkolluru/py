import time
from datetime import datetime as dt

time.sleep(35)

hosts_path = '/etc/hosts'

redirect = '127.0.0.1'

block_site_list = [
    'www.facebook.com', 'facebook.com', 'mail.google.com', 'studio.youtube.com',
    'www.youtube.com', 'www.primevideo.com', 'www.amazon.in', 'www.flipkart.com',
    'www.myntra.com', 'www.jabong.com', 'www.imdb.com', 'www.netflix.com'
]

if 0 <= dt.weekday(dt.now()) < 5 and 10 <= dt.now().hour <= 20: # Weekdays are numbered from 0 to 6 Starting from Monday = 0 to Sunday = 6
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


# /home/gautham/Documents/CodingLabs/pybench/Automation/website_blocker.py