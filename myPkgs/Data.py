import os


class Path:
    identifierJson = ""
    driver = "myData/chromedriver.exe"
    profile = os.getcwd()+"/myData/chromeProfile/"

    infoList="myData/infoList.pickle"
    infoDictList="myData/infoDictList.pickle"
    infoListAdjusted="myData/infoListAdjusted.pickle"
    newArrival="myData/newArrival.pickle"

    emailTargetFile="myData/emailTarget.txt"

    templateHeader="Template/header.html"
    templateItem="Template/item.html"
    templateFooter="Template/Footer.html"


class Scrap:

    title = "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[{0}]/div/div[1]/table/tbody/tr/td[2]/a"
    LatestChapter = "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[{0}]/div/div[1]/table/tbody/tr/td[2]/div[1]/span/a"
    LatestDate = "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[{0}]/div/div[1]/table/tbody/tr/td[2]/div[1]/span/span"
    LastRead = "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[{0}]/div/div[1]/table/tbody/tr/td[2]/div[2]/span/a"

    title2 = "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[4]/div/div[1]/table/tbody/tr/td[2]/a"

    titleClass ="SubBox"

    subscriptionsPage="https://mangasee123.com/user/subscription.php"

    subscriptionsSize="/html/body/div[2]/div/div/div/div[1]/span"

    baseUrl="https://mangasee123.com"

class Const:

    title="title"
    latest="latest"
    latestDate="latestDate"
    lastRead="lastRead"

    linkTitle="linkTitle"
    linkLatest="linkLatest"
    linkLastRead="lastRead"

    class Email:
        subject="manga see feed."

        mailServer="smtp.gmail.com:587"

class Info:
    title=None
    latest=None
    lastRead=None
    latestDate=None

    linkTitle=None
    linkLatest=None
    linkLastRead=None