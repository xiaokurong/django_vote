# -*- coding: UTF8 -*-
import time
import datetime
import os
import shutil
import gl


def TimeStampToTime(timestamp):
    timeStruct=time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

def getFileCreateTime(filePath):
    # filePath=unicode(filePath,'utf8')
    t2=os.path.getctime(filePath)
    return t2

def getTimeStamp(atime):
    t1 = time.mktime(time.strptime(atime,'%Y-%m-%d %H:%M:%S'))
    return t1

def fileCopy(sourcePath,targetPath):
    #start='2019-05-01 20:20:00'
    #end='2019-06-01 00:00:00'
    
    if not os.path.exists(sourcePath):
        return
    if not os.path.exists(targetPath):
        os.makedirs(targetPath)

    for fileName in os.listdir(sourcePath):
        absourcePath=os.path.join(sourcePath,fileName)
        abstargetPath=os.path.join(targetPath,fileName)
        if os.path.isdir(absourcePath):
            fileCopy(absourcePath,abstargetPath)

        if os.path.isfile(absourcePath):
            fileCreateTime=getFileCreateTime(absourcePath)
            startTime=getTimeStamp(gl.start)
            endTime=getTimeStamp(gl.end)
            if startTime< fileCreateTime and fileCreateTime <endTime :
                shutil.copy(absourcePath,abstargetPath)
            else:
                continue
            

def judgeFile(sourcePath,timea,timeb):
    pass

def main():
    #start='2019-09-01 20:30:00'
    #end='2019-09-02 20:30:00'
    # sourcePath = 'D:\mysql_bak'
    # targetPath='D:\mysql_month_bak'
    fileCopy(gl.sourcePath,gl.targetPath)
    print("copy files ending.")
    #print(getTimeStamp(startTime))

            

        
    #for filename in os.listdir(dirPath):
    #    print('filename is :',filename)
    #print(getFileCreateTime(filePath))
    


if __name__ == "__main__":
    main()
