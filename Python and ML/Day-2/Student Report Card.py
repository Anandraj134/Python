def grading(x):
    j = 0
    subject = []
    marks = []
    while j < x:
        sub = input("Enter Subject Name :- ")
        mar = int(input("Enter Mark :- "))
        subject.append(sub)
        marks.append(mar)
        j += 1
    return subject, marks


i = 0
s = int(input("Enter the number of students :- "))
while i < s:
    st = int(input("Enter Total no. of subject for Student-{}".format(i+1)))
    subject, marks = grading(st)
    print("Report Card of Student-{0}".format(i+1))
    for x in range(len(subject)):
        print("{0} -> {1}".format(subject[x], marks[x]))
    i += 1
