from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import winsound
import threading
import webbrowser
import telegram
import os

class AsyncTask:
    def __init__(self):
        self.my_token = []
        self.bot = []
        self.targetUrl = []
        self.url = []
        pass

    def SetupFile(self):
        f = open('prevLink.txt', 'a')
        f.close()

    def SetupBrowser(self):
        self.targetUrl = "http://www.ppomppu.co.kr/zboard/"
        self.url = "http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu"

    def SetupTelegram(self):
        self.my_token = 'Token'
        self.bot = telegram.Bot(token=self.my_token)
        threading.Timer(60, self.SetupTelegram).start()

    def FindHappy(self):
        str = "해피머니"
        html = urlopen(self.url)
        bsObject = BeautifulSoup(html, "html.parser")

        for link in bsObject.find_all('a'):
            if link.text.find(str) != -1:
                if link.text.find("[") != -1:
                    os.system('cls')
                    urlData = self.targetUrl + link.get('href')
                    read = open('prevLink.txt', mode='r', encoding='utf-8')

                    findLink = link.get('href').split('&no=')[1];
                    prevLink = read.readline();
                    read.close()

                    if(findLink != prevLink):
                        f = open('prevLink.txt', mode='wt', encoding='utf-8')
                        f.write(findLink)
                        f.close()
                        webbrowser.open(urlData)
                        for i in range(0, 5):
                            self.bot.sendMessage(chat_id='@HappyObserver',
                                                 text=(link.text.strip(), urlData))
                    break

        print("Try Finding")
        threading.Timer(5, self.FindHappy).start()


at = AsyncTask()
at.SetupFile()
at.SetupBrowser()
at.SetupTelegram()
at.FindHappy()
