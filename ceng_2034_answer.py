from threading import Thread
import os
from queue import Queue
import requests
from time import time

print(os.getpid())

load1, load5, load15 = os.getloadavg()

Last5=load5

Core=os.cpu_count()

if (Core-Last5) < 1:
 exit()

sira = Queue()

urls = ["http://api.github.com",
        "http://bilgisayar.mu.edu.tr",
        "http://python.org",
        "http://akrepnalan.com/ceng2034",
        "http://github.com/caesarsalad/wow"]

start = time()
def checksite (que):

    while True:
        url = que.get()
        check = requests.get(url)
        if 200 <= check.status_code and check.status_code < 300:
            print(url, "is valid")
        else:
         print(url, "is not valid")
        que.task_done()

if __name__ == "__main__":
    basla = time() 
    for i in range(5):
        t = Thread(target = checksite, args = (sira,))
        t.daemon = True
        t.start()

    for url in urls:
        sira.put(url)

    sira.join()

print ( (time() - basla), "saniye surdu")