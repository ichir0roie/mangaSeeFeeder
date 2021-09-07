import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from myPkgs.Data import *

import pickle

class Mailer:
    def __init__(self):
        print("mailer")
        self.infoList=[]
        self.accountList=[]

        self.templateHeader=""
        self.templateItem=""
        self.templateFooter=""

        self.newArrival=0

    # sendMail

    def run(self):
        self.setupMailer()

        for account in self.accountList:
            self.sendMail(account)


    def sendMail(self,emailData:dict):
        message=MIMEMultipart('alternative')
        message["subject"]=Const.Email.subject
        message["To"]=emailData["email"]
        message["From"]=emailData["email"]
        message.preamble="this is why?"

        body=self.getBody(self.infoList)

        htmlBody=MIMEText(body,'html')
        message.attach(htmlBody)

        server=smtplib.SMTP(Const.Email.mailServer)
        server.starttls()
        server.login(emailData["email"],emailData["password"])
        server.sendmail(emailData["email"],[emailData["email"]],message.as_string())
        server.quit()

    # setupMailer

    def getBody(self,infoList:list):
        bodyText=""
        # set header

        bodyText+=self.templateHeader.format(
            newArrival=self.newArrival
        )

        for info in infoList:
            bodyText+=self.getHtmlFromInfo(info)

        # set footer

        bodyText+=self.templateFooter

        return bodyText

    def getHtmlFromInfo(self,info:Info):
        itemText=self.templateItem.format(
            title=info.title,
            latest=info.latest,
            latestDate=info.latestDate,
            lastRead=info.lastRead,
            linkTitle=info.linkTitle,
            linkLatest=info.linkLatest,
            linkLastRead=info.linkLastRead
        )
        return itemText

    def setupMailer(self):
        with open(Path.emailTargetFile,"r",encoding="utf-8",)as f:
            accounts=f.read().splitlines()
        print(accounts)
        accountList=[]
        try:
            for account in accounts:
                email,password=account.split(",")
                if email=="email":
                    continue
                data={"email":email,"password":password}
                accountList.append(data)
        except Exception as e:
            print(e)
            print("emailTarget format is wrong.")
        print(accountList)
        self.accountList=accountList

        self.loadTemplates()
        self.loadInfo()

    def loadTemplates(self):
        with open(Path.templateHeader,mode="r",encoding="utf-8")as f:
            self.templateHeader=f.read()
        with open(Path.templateItem,mode="r",encoding="utf-8")as f:
            self.templateItem=f.read()
        with open(Path.templateFooter,mode="r",encoding="utf-8")as f:
            self.templateFooter=f.read()

    def loadInfo(self):
        with open(Path.infoListAdjusted,"rb")as f:
            self.infoList=pickle.load(f)
        with open(Path.newArrival,"rb")as f:
            self.newArrival=pickle.load(f)

    def testGetBody(self):
        self.setupMailer()
        print(self.getBody(self.infoList))


if __name__ == '__main__':
    mailer=Mailer()
    mailer.run()