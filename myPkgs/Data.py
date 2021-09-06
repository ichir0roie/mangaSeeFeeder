import os


class Path:
    identifierJson = ""
    driver = "myData/chromedriver.exe"
    profile = os.getcwd()+"/myData/chromeProfile/"


class Config:
    email = "ichir0roie@gmail.com"


class Scrap:

    title = "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[{0}]/div/div[1]/table/tbody/tr/td[2]/a"
    LatestChapter = "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[{0}]/div/div[1]/table/tbody/tr/td[2]/div[1]/span/a"
    LatestDate = "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[{0}]/div/div[1]/table/tbody/tr/td[2]/div[1]/span/span"
    LastRead = "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[{0}]/div/div[1]/table/tbody/tr/td[2]/div[2]/span/a"

    title2 = "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[4]/div/div[1]/table/tbody/tr/td[2]/a"

    titleClass ="SubBox"

    subscriptionsPage="https://mangasee123.com/user/subscription.php"

    subscriptionsSize="/html/body/div[2]/div/div/div/div[1]/span"

class Const:
    title="title"
    latest="latest"
    latestDate="latestDate"
    lastRead="lastRead"
