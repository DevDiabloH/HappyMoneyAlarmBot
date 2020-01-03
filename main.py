from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import winsound
import threading
import webbrowser
import os
import telegram


class AsyncTask:
    def __init__(self):
        self.my_token = []
        self.bot = []
        self.data = []
        self.targetUrl = []
        self.url = []
        pass

    def SetupBrowser(self):
        self.targetUrl = "http://www.ppomppu.co.kr/zboard/"
        self.url = "http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu"

    def SetupTelegram(self):
        self.my_token = 'YourToken'
        self.bot = telegram.Bot(token=self.my_token)
        threading.Timer(60, self.SetupTelegram).start()

    def FindHappy(self):
        findStr = "해피머니"
        html = urlopen(self.url)
        bsObject = BeautifulSoup(html, "html.parser")

        for link in bsObject.find_all('a'):
            if link.text.find(findStr) != -1:
                if link.text.find("[") != -1:
                    os.system('cls')
                    if self.data != self.targetUrl + link.get('href'):
                        print(link.text.strip(), targetUrl + link.get('href'))
                        self.data = self.targetUrl + link.get('href')
                        webbrowser.open(self.targetUrl + link.get('href'))
                        for i in range(0, 9):
                            self.bot.sendMessage(chat_id='@HappyObserver', text=(self.targetUrl + link.get('href')))
                    break

        print("Try Finding")
        threading.Timer(20, self.FindHappy).start()


at = AsyncTask()
at.SetupBrowser()
at.SetupTelegram()
at.FindHappy()
