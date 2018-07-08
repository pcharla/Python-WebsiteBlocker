import time
from datetime import datetime as dt
hosts_temp='hosts.txt'
#hosts_path= r'C:\windows\System32\drivers\etc\hosts'
redirect= '127.0.0.1'
websites=['www.facebook.com','facebook.com','www.amazon.com','amazon.com']
while True:
  if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,18):
    print('working hours')
    with open(hosts_temp,'r+') as file:
      content= file.read()
      for website in websites:
        if website in content:
          pass
        else:
          file.write(redirect +' '+ website + '\n')
  else:
    with open(hosts_temp,'r+') as file:
      content= file.readlines()
      file.seek(0)
      for line in content:
        if not any ( website in line for website in websites):
          file.write(line)
      file.truncate()
    print('free enjoy')
  time.sleep(5)
