import json
import os
print("CAT: Hello! I am CAT. CAT stands for Chat AI Thing. ")
name=input("CAT: What is your name? \nYour name: ")
folder="userCATdata"
if not os.path.exists(folder):
    os.makedirs(folder)
filePath=os.path.join(folder,f"{name}'s CAT data.json")
if os.path.exists(filePath):
    print(f"CAT: Nice to see you again {name}. ")
    with open(filePath) as fileHandle:
        userInputs=json.load(fileHandle)
else:
    userInputs={}
    print(f"CAT: Nice to meet you {name}. I'm still learning so please be patient with me. ")
files=[f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder,f))]

listOfDictionariesOfCATuserFiles=[]
#for file in files:
#    with open(os.path.join(folder,file)) as userFile:
#        listOfDictionariesOfCATuserFiles.append(json.load(userFile))
#userVotes={}
#for CATuserFile in listOfDictionariesOfCATuserFiles:
#    for key, value in CATuserFile.items():
#        if userVotes[key]>=0:
#            userVotes[key]=userVotes[key]+1
#        else:
#            userVotes[key]=0
x=0
while True:
    x=x+1
    userInput=input(f"{name}: ")
    if userInput in userInputs:
        print("CAT: "+userInputs[userInput])
    else:
        correctOutput=input("CAT: I haven't heard that from you before! What would be appropriate to say here? \nAppropriate response: ")
        userInputs[userInput]=correctOutput
        with open(filePath,"w") as fileHandle:
            json.dump(userInputs,fileHandle)