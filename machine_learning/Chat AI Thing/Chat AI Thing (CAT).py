import json
import os
import random

# Greeting
votingThreshold = 0.5
print("CAT: Hello! I am CAT. CAT stands for Chat AI Thing.")
name = input("CAT: What is your name? \nYour name: ")
while name.strip() == "":
    name = input("CAT: Your name cannot be empty! \nYour name: ")

# File and folder setup
folder = "userCATdata"
if not os.path.exists(folder):
    os.makedirs(folder)

filePath = os.path.join(folder, f"{name}'s CAT data.json")

# Load or initialize userInputs
if os.path.exists(filePath):
    print(f"CAT: Nice to see you again, {name}.")
    with open(filePath) as fileHandle:
        userInputs = json.load(fileHandle)
else:
    userInputs = {}
    print(f"CAT: Nice to meet you, {name}. I'm still learning, so please be patient with me.")

# Load data from all user files to generate voting statistics
files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
listOfDictionariesOfCATuserFiles = []
for file in files:
    with open(os.path.join(folder, file)) as userFile:
        listOfDictionariesOfCATuserFiles.append(json.load(userFile))

# Global dictionary to store vote counts
userVotes = {}

def updateUserVotes():
    global userVotes
    userVotes = {}
    for CATuserFile in listOfDictionariesOfCATuserFiles:
        for key, value in CATuserFile.items():
            if key not in userVotes:
                userVotes[key] = {}
            userVotes[key][value] = userVotes[key].get(value, 0) + 1

def overwriteNewInput(question, userInput):
    correctOutput = input(question)
    userInputs[userInput] = correctOutput

    # Save the user's response to their data file
    with open(filePath, "w") as fileHandle:
        json.dump(userInputs, fileHandle)

    # Update userVotes immediately
    if userInput not in userVotes:
        userVotes[userInput] = {}
    userVotes[userInput][correctOutput] = userVotes[userInput].get(correctOutput, 0) + 1

# Initialize votes
updateUserVotes()

# Main chat loop
while True:
    userInput = input(f"{name}: ").strip()
    if userInput == "":
        continue

    # If the input is recognized, print the stored response
    if userInput in userInputs:
        print("CAT:", userInputs[userInput])

        # Occasionally ask for feedback
        if random.randint(0, 100) <= 5:
            feedback = input("CAT: Was that right? (Y/N) ").strip().upper()
            if feedback == "N":
                overwriteNewInput("CAT: What would be appropriate to say here? \nAppropriate response: ", userInput)
    else:
        overwriteNewInput("CAT: I haven't heard that from you before! What would be appropriate to say here? \nAppropriate response: ", userInput)

    # Now check the votes before responding
    if userInput in userVotes:
        voteData = userVotes[userInput]
        mostVotedResponse = max(voteData, key=voteData.get)
        amountOfTimeMostVotedResponseVoted = voteData[mostVotedResponse]

        # Print vote data for debugging
        print("Vote data for this input:", voteData)
        print("Most voted response:", mostVotedResponse, "\nAmount of times most voted response voted:", amountOfTimeMostVotedResponseVoted)

        # Decide what to do based on the votes
        if amountOfTimeMostVotedResponseVoted > 1:
            # Check if the vote proportion is enough to meet the threshold
            if amountOfTimeMostVotedResponseVoted / sum(voteData.values()) >= votingThreshold:
                print(f"CAT: {mostVotedResponse}")  # Actually say the most voted response
            else:
                # Ask for clarification using the existing message
                overwriteNewInput("CAT: I haven't heard that from you before! What would be appropriate to say here? \nAppropriate response: ", userInput)
        else:
            print("CAT: Not enough votes, declined for troll prevention.")  # Troll prevention

    else:
        print(f"CAT: No votes recorded for '{userInput}' yet.")  # No votes yet for the input
