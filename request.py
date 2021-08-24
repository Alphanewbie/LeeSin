import requests
import time
from bs4 import BeautifulSoup

urls = []
urls.append("https://cordingtrend.azurewebsites.net/mains")
urls.append("http://127.0.0.1:8000/mains")

for _ in range(1) :
    for url in urls:
        print(url + " - test")
        i = 1
        while True:
            try:
                i += 1
                responce = requests.get(url)
                soup = BeautifulSoup(responce.text, 'html.parser')
                is_in = soup.select("body > div > div > a")
                if not is_in:
                    raise IOError
                print("success!!")
                break
            except:
                if i == 10:
                    print("Fail")
                    exit()
                else:
                    print("Retry")
                    time.sleep(1)
        print(url + " - end")
        responce = requests.get(url + "/issue")
        print(url + "/issue - end")
        responce = requests.get(url + "/repository")
        print(url + "/repository - end")
        if url != "http://127.0.0.1:8000/mains" :
            responce = requests.get(url + "/setting")
            print(url + "/setting - end")
        # responce = requests.get(url + "/crawling")
        # print(url + "/crawling - end")
