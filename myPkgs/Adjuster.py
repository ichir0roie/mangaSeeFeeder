

from myPkgs.Data import *
import pickle

class Adjuster:
    def __init__(self):
        self.infoList=[]
        self.infoListAdjusted=[]
        with open(Path.infoDictList,"rb")as f:
            self.infoDictList=pickle.load(f)
        with open(Path.infoList,"rb")as f:
            self.infoList=pickle.load(f)


    def setUnread(self):
        self.infoListAdjusted=[]
        for info in self.infoList:
            latest=float(info.latest)
            lastRead=float(info.lastRead)
            if lastRead<latest:
                self.infoListAdjusted.append(info)

        newArrival=len(self.infoListAdjusted)

        with open(Path.newArrival,mode="wb")as f:
            pickle.dump(newArrival,f)


        with open(Path.infoListAdjusted,mode="wb")as f:
            pickle.dump(self.infoListAdjusted,f)

    def getAdjustedList(self):
        return self.infoListAdjusted

    def printInfoList(self, infoDictList:list):
        text="|"
        if len(infoDictList)==0:
            return
        for key in infoDictList[0].keys():

            if key == Const.title:
                if len(key) > 23:
                    val = key[:20] + "..."
                else:
                    while len(key) < 24:
                        key += ' '
            else:
                while len(key) < 15:
                    key += ' '
            text+=key+"\t|\t"
        print(text)
        line="|"
        for i in range(len(text)):
            line+="-"
        line+="-----|"
        print(line)

        for info in infoDictList:
            text="|"
            for key in info.keys():
                val=info[key]
                if key==Const.title:
                    if len(val)>23:
                        val=val[:20]+"..."
                    else:
                        while len(str(val))<23:
                            val+=' '
                else:
                    while len(str(val)) < 15:
                        val += ' '
                text+=val+"\t|\t"
            print(text)

        print(line)

    def viewAllAndAdjust(self):
        print("all data")
        adj.printInfoList(adj.infoDictList)

if __name__ == '__main__':
    adj=Adjuster()
    adj.setUnread()
    adj.viewAllAndAdjust()