import pract1

pract1.SetTestData(set([
    pract1.Student(b"Shcherbak N.O.", b"SE-20-1", [pract1.Subject(b"VMPTF", 10), pract1.Subject(b"APZ", 10), pract1.Subject(b"PvIT", 10)], 50000),
    pract1.Student(b"Smith J.", b"SE-20-11", [pract1.Subject(b"VMPTF", 8), pract1.Subject(b"APZ", 2), pract1.Subject(b"PvIT", 5)], 20000),
    pract1.Student(b"Jinping X.", b"SE-20-12", [pract1.Subject(b"VMPTF", 2), pract1.Subject(b"APZ", 2), pract1.Subject(b"PvIT", 10)], 100000)
]))

pract1.LaunchTest()