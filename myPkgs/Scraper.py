from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver

import os

from myPkgs.Data import *
import time

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
            info={}
            info[Const.title]=aText[1]
            info[Const.latest]=aText[2]
            info[Const.lastRead]=aText[3]

            spanData=subscription.find_elements_by_tag_name("span")
            if len(spanData)<2:
                continue
            info[Const.latestDate]=spanData[1].text.replace("· ","")

            infoList.append(info)


        print("subscriptions is over")

        for i in infoList:
            print(i)

        # todo:save infoList to pickle

    # def getSubscriptionInfo(self,subscription):


if __name__ == '__main__':
    import os
    scraper = Scraper()
    scraper.setSubscriptionsPage()
    scraper.getInfoFromSubScriptions()

    # scraper.wait()
