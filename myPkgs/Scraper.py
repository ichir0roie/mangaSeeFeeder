import pickle
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from myPkgs.Data import *

import urllib.parse as up


class Scraper:
    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=' + Path.profile)
        options.add_argument('--disable-features=InfiniteSessionRestore')
        # options.add_argument('--headless')

        self.driver = webdriver.Chrome(
            options=options, executable_path=Path.driver)

    def getPage(self, url):
        self.driver.get(url)

    def setSubscriptionsPage(self):
        self.driver.get(Scrap.subscriptionsPage)

    def wait(self):
        input("please any")

    def getInfoFromSubScriptions(self):
        d = self.driver

        infoList=[]
        infoDictList=[]

        try:
             subscriptionsSize= WebDriverWait(scraper.driver, 60 * 15).until(
                EC.presence_of_element_located((By.XPATH, Scrap.subscriptionsSize))
            )
        finally:
            print("scraping start")

        subscriptionsSize=subscriptionsSize.text.replace("(","").replace(")","")
        subscriptionsSize=int(subscriptionsSize)

        subscriptions = d.find_elements_by_class_name(Scrap.titleClass)
        while subscriptionsSize!=len(subscriptions):
            d.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)
            subscriptions = d.find_elements_by_class_name(Scrap.titleClass)

        for subscription in subscriptions:
            aData = subscription.find_elements_by_tag_name("a")
            aText=[aElem.text for aElem in aData]

            if len(aText)<4:
                continue

            info=Info()
            info.title=aText[1]
            info.latest=aText[2]
            info.lastRead=aText[3]

            # set links
            urlText=[
                up.urljoin(Scrap.baseUrl,aElem.get_attribute("href"))
                for aElem in aData
            ]
            info.linkTitle=urlText[1]
            info.linkLatest=urlText[2]
            info.linkLastRead=urlText[3]


            infoDict={}
            infoDict[Const.title]=aText[1]
            infoDict[Const.latest]=aText[2]
            infoDict[Const.lastRead]=aText[3]

            spanData=subscription.find_elements_by_tag_name("span")
            if len(spanData)<2:
                continue
            info.latestDate=spanData[1].text.replace("· ","")
            infoDict[Const.latestDate]=spanData[1].text.replace("· ","")


            infoConverted=self.convertInfo(info)
            infoList.append(infoConverted)

            infoDictConverted=self.convertInfoDict(infoDict)
            infoDictList.append(infoDictConverted)

        print("subscriptions is over")

        for i in infoList:
            print(i)

        # save infoList to pickle

        with open(Path.infoList,mode="wb")as f:
            pickle.dump(infoList,f)
        with open(Path.infoDictList,mode="wb")as f:
            pickle.dump(infoDictList,f)


    def convertInfo(self,info:Info):
        latest=info.latest
        latest=latest.replace("Chapter ","")
        info.latest=latest

        lastRead=info.lastRead
        if "Ongoing " in lastRead:
            info.lastRead="0"
        else:
            lastRead=lastRead.replace("Chapter ","")
            info.lastRead=lastRead

        return info


    def convertInfoDict(self,info:dict):
        latest=info[Const.latest]
        latest=latest.replace("Chapter ","")
        info[Const.latest]=latest

        lastRead=info[Const.lastRead]
        if "Ongoing " in lastRead:
            info[Const.lastRead]="0"
        else:
            lastRead=lastRead.replace("Chapter ","")
            info[Const.lastRead]=lastRead
        return info

    # def getSubscriptionInfo(self,subscription):

    def close(self):
        print("driver is quit.")
        self.driver.quit()

if __name__ == '__main__':
    scraper = Scraper()
    scraper.setSubscriptionsPage()
    scraper.getInfoFromSubScriptions()
    scraper.close()
