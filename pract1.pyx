from libc.stdio cimport sprintf
import pickle
import os

cdef class Subject:
    cdef public char* name;
    cdef public int grade;
    
    def __init__(self, char* name, int grade):
        self.name = name
        self.grade = grade
    
    cpdef char* catFields(self):
        cdef char grade_buf[4]
        sprintf(grade_buf, "%d", self.grade)
        return self.name + b". Оцінка: " + grade_buf

cdef class Student:
    cdef public char* name
    cdef public char* group
    cdef public set subjects
    cdef public float scholarship

    def __init__(self, name, group, subjects, scholarship):
        self.name = name
        self.group = group
        self.scholarship = scholarship
        self.subjects = set()

        cdef int i = 0
        while(i < len(subjects)):
            self.subjects.add(subjects[i])
            i += 1

    cpdef float tryReduceScholarship(self):
        cdef float redAmmount
        for subj in self.subjects:
            if subj.grade <= 2:
                redAmmount = self.scholarship*0.2
                self.scholarship -= redAmmount
                return redAmmount
        return 0

    cpdef printme(self):
        print("Ім'я: {0}, група: {1}, дисципліни: {2}, стипендія: {3} ".format(self.name.decode('utf-8'), self.group.decode('utf-8'), 
                                                                               [subj.catFields().decode('utf-8') for subj in self.subjects], self.scholarship))
cdef void writeStudentsToTestFile(set data):
    with open('data', 'wb') as fout:
        pickle.dump(data, fout)
    fout.close()

cdef set readStudentsFromTestFile():
    cdef set loadedData
    with open('data', 'rb') as fin:
        loadedData = pickle.load(fin)
    fin.close()
    return loadedData

cdef set tryChangeScholarShip(set students):
    for stud in students:
        if stud.tryReduceScholarship() != 0:
            print("Зменшено стипендію у студена {0}".format(stud.name.decode('utf-8')))
    return students

cpdef void SetTestData(set students):
    writeStudentsToTestFile(students)

cpdef void LaunchTest():
    cdef set students = readStudentsFromTestFile()
    if len(students) == 0:
        print("An error occured when reading a file or the file is empty.")
        return
    
    students = tryChangeScholarShip(students)
    writeStudentsToTestFile(studentsToWrite)
    
    students = readStudentsFromTestFile()
    for stud in students:
        stud.printme()