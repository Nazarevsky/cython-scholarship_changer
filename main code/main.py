import pickle
import os.path as p

FILE_NAME = "data"

class Subject:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def toString(self):
        return "{0}. Оцінка: {1}".format(self.name, self.grade)

class Student:
    def __init__(self, name, group, subjects, scholarship):
        self.name = name
        self.group = group
        self.subjects = subjects
        self.scholarship = scholarship

    def tryReduceScholarship(self):
        for subj in self.subjects:
            if subj.grade <= 2:
                redAmmount = self.scholarship*0.2
                self.scholarship -= redAmmount
                return redAmmount
        return 0
            
    def print(self):
        print("Ім'я: {0}, група: {1}, дисципліни: {2}, стипендія: {3} ".format(self.name, self.group, 
                                                                               [subj.toString() for subj in self.subjects], self.scholarship))

def writeData(data):
    f = open(FILE_NAME, 'wb')
    pickle.dump(data, f)
    f.close()

def tryCreateTestFile():
    if p.isfile(FILE_NAME) == False:
        dataToWrite = [
            Student('Щербак Н.О.', 'ПЗПІ-20-1', [Subject('ВМПТФ', 10), Subject('АПЗ', 10), Subject('ПвІТ', 10)], 50000),
            Student('П\'яточкін О.М.', 'ПЗПІ-20-11', [Subject('ВМПТФ', 8), Subject('АПЗ', 2), Subject('ПвІТ', 5)], 20000),
            Student('Цзіньпін С.', 'ПЗПІ-20-12', [Subject('ВМПТФ', 2), Subject('АПЗ', 2), Subject('ПвІТ', 10)], 100000)
        ]
        writeData(dataToWrite)

def readStudentsFromTestFile():
    f = open(FILE_NAME, 'rb')
    return pickle.load(f)

def tryChangeScholarShip(students):
    for stud in students:
        if stud.tryReduceScholarship() != 0:
            print("Зменшено стипендію у студена {0}".format(stud.name))
    return students

def LaunchPract1():
    tryCreateTestFile()
    students = readStudentsFromTestFile()
    students = tryChangeScholarShip(students)
    writeData(students)

    changedStudents = readStudentsFromTestFile()
    for stud in changedStudents:
        stud.print()

LaunchPract1()