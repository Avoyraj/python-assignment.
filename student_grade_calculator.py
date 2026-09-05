name =input("enter your name")                                                                     
subject1 =float(input("enter your subject1 marks"))
subject2 =float(input("enter your subject2 marks"))
subject3 =float(input("enter your subject3 marks"))

total_marks = subject1 + subject2 + subject3
average_marks = total_marks / 3
if average_marks >= 80:
    print("Your grade is A+")
elif average_marks >= 70:
    print("Your grade is A")
elif average_marks >= 60:
    print("Your grade is B")
elif average_marks >= 50:
    print("Your grade is c")