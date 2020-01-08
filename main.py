from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import threading
import webbrowser
import os
import telegram

class AsyncTask:
    def __init__(self):
        self.my_token = []
        self.bot = []
        self.targetUrl = []
        self.str = []
        self.url = []
        pass

    def SetupTextFile(self):
        saveLink = open('prevLink.txt', 'a')
        saveLink.close()

        try:
            self.FindItemUpdate()
        except:
            findItem = open('findItem.txt', 'a')
            findItem.close()
            self.str = ""

    def FindItemUpdate(self):
        findItem = open('findItem.txt', mode='r', encoding='utf-8')
        self.str = findItem.readline()
        findItem.close()

    def SetupURL(self):
        self.targetUrl = "http://www.ppomppu.co.kr/zboard/"
        self.url = "http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu"

    def SetupTelegram(self):
        self.my_token = 'TOKEN'
        self.bot = telegram.Bot(token=self.my_token)
        threading.Timer(60, self.SetupTelegram).start()

    def FindHappy(self):
        html = urlopen(self.url)
        bsObject = BeautifulSoup(html, "html.parser", from_encoding='utf-8')

        if(self.str == ""):
            print("What do you want find item? write in findItem.txt")
            self.FindItemUpdate()
        else:
            for link in bsObject.find_all('a'):
                if link.text.find(self.str) != -1:
                    if link.text.find("[") != -1:
                        os.system('cls')
                        urlData = self.targetUrl + link.get('href')
                        read = open('prevLink.txt', mode='r', encoding='utf-8')

                        findLink = link.get('href').split('&no=')[1];
                        prevLink = read.readline();
                        read.close()

                        if (findLink != prevLink):
                            f = open('prevLink.txt', mode='wt', encoding='utf-8')
                            f.write(findLink)
                            f.close()
                            webbrowser.open(urlData)
                            for i in range(0, 5):
                                self.bot.sendMessage(chat_id='@HappyObserver',
                                                     text=(link.text.strip(), urlData))
                        break
            print("Try Finding")

        threading.Timer(30, self.FindHappy).start()



at = AsyncTask()
at.SetupTextFile()
at.SetupURL()
at.SetupTelegram()
at.FindHappy()
