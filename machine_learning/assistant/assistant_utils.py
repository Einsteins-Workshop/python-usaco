import json
def print_data(file):
    with open(file, "r") as fileHandle:
        print(fileHandle.read())


def get_data(file):
    with open(file, "r") as fileHandle:
        return json.loads(fileHandle.read())


def add_student(database):
    records = database['database']
    number_of_records=len(records)
    new_student = {
        'user_number' : number_of_records + 1,
        'name' : input("What is your name?")
    }


    grade = input("What grade are you in?")
    physical_attributes = input("Please type in your physical strengths")


    new_student['grade'] = grade
    new_student['physical_attributes']=physical_attributes
    records.append(new_student)
    return database


def write_data_to_file(database, file):
    with open(file, "w") as fileHandle:
        fileHandle.write (json.dumps(database))
