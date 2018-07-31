import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = '127.0.0.1'
sites_that_kill_me = ['www.facebook.com', 'facebook.com', 'gmail.com', 'www.gmail.com']
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,17):
        print('Working Time!!')
        with open(hosts_path,'r+') as file:
            content = file.read()
            for site in sites_that_kill_me:
                if site in content:
                    pass
                else:
                    file.write(redirect + ' ' + site + '\n')
        time.sleep(60000)
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in sites_that_kill_me):
                    file.write(line)
            file.truncate()
        print('Time to play')
        time.sleep(60000)





