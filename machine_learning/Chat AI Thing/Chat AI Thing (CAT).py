import json
import os
print("CAT: Hello! I am CAT. CAT stands for Chat AI Thing. ")
name=input("CAT: What is your name? \nYour name: ")
folder="catUserFiles"
if not os.path.exists(folder):
    os.makedirs(folder)
filePath=os.path.join(folder,f"{name}'s file")
if os.path.exists(filePath):
    print(f"CAT: Nice to see you again {name}. ")
    with open(filePath) as fileHandle:
        userInputs=json.load(fileHandle)
else:
    userInputs={}
    print(f"CAT: Nice to meet you {name}. I'm still learning so please be patient with me. ")
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