import json
import os
print("CAT: Hello! I am CAT. CAT stands for Chat AI Thing. ")
name=input("CAT: What is you name? \nYour name: ")
if os.path.exists(f"{name}'s file"):
    print(f"CAT: Nice to see you again {name}. ")
    with open(f"{name}'s file") as fileHandle:
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
        with open(f"{name}'s file","w") as fileHandle:
            json.dump(userInputs,fileHandle)
