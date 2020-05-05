import os
import requests

print(os.getpid())

load1, load5, load15 = os.getloadavg()

Last5=load5

Core=os.cpu_count()

if (Core-Last5) < 1:
 exit()

urls = ["http://api.github.com",
        "http://bilgisayar.mu.edu.tr",
        "http://python.org",
        "http://akrepnalan.com/ceng2034",
        "http://github.com/caesarsalad/wow"]
 
for x in urls:
  check = requests.get(x)
  if 200 <= check.status_code and check.status_code < 300:  
    print (x, "is valid")
  else:
    print (x, "is not valid")