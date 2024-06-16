""""This program will calculate the Grade Point Average of a student in the University of Ghana."""

# Will have to first get the courses the student is offering first.

courses = []
hours = []
grades = []
gradePoint = []

try:
    numberOfCourses = int(input("Enter the number of courses you offer: \n"))

    # Created a function to get the courses the student offers
    def course_select():
        begin = 0
        while begin != numberOfCourses:
            ask = input("Please enter the course you offer: \n")
            courses.append(ask.upper())
            begin += 1
            print(courses)


    course_select()
    # Checks if the courses the student entered is correct

    print("There these the courses you offer? \n")


    def list_make():
        for course in courses:
            print(course)


    list_make()
    response = input("Y = Yes or N = No: \n")

    if response.upper() == 'Y':
        print("Very good! Let continue then.")

        # Entering of credit hours
        begin = 0
        while begin != numberOfCourses:
            print("Please enter the credit hours for the following courses: ")
            list_make()
            time = input(">>")
            hours.append(int(time))
            begin += 1
            print(hours)
        print("Very Good. Let's move on.")
        print("These are the courses and their respective credit hours.")
        for course, hour in zip(courses, hours):
            print(course, ": ", hour)

        total_credit = sum(hours)

        # Entering of Grades
        print("Please enter the grades you had in the following courses respectively.")
        print(courses)

        begin = 0
        while begin != numberOfCourses:
            ask_grade = input(">>")
            grades.append(ask_grade.upper())
            begin += 1
        print(grades)

        # Determination of grade points based on grades(A, B, C, D,...) entered
        for hour, grade in zip(hours, grades):
            if grade.upper() == "A":
                gpt = hour * 4.0
                gradePoint.append(gpt)
            elif grade.upper() == "B+":
                gpt = hour * 3.5
                gradePoint.append(gpt)
            elif grade.upper() == "B":
                gpt = hour * 3.0
                gradePoint.append(gpt)
            elif grade.upper() == "C+":
                gpt = hour * 2.5
                gradePoint.append(gpt)
            elif grade.upper() == "C":
                gpt = hour * 2.0
                gradePoint.append(gpt)
            elif grade.upper() == "D+":
                gpt = hour * 1.5
                gradePoint.append(gpt)
            elif grade.upper() == "D":
                gpt = hour * 1.0
                gradePoint.append(gpt)
            elif grade.upper() == "E":
                gpt = hour * 0.5
                gradePoint.append(gpt)
            elif grade.upper() == "F":
                gpt = hour * 0.0
                gradePoint.append(gpt)
            else:
                print("Something went wrong :(")

        totalGradePoint = sum(gradePoint)
        gpa = round(totalGradePoint / total_credit, 2)
        print("Your GPA is ", gpa)

        # Break down of grading
        print("Would like to view the break of your course? \nY=Yes N=No \n")
        answer = input(">>")

        if answer.upper() == "Y":
            print("Course ", " ", "Credit", " ", "Grade", " ", "Grade point")
            for course, hour, grade, point in zip(courses, hours, grades, gradePoint):
                print(course, "\t\t", hour, "\t\t", grade, "\t\t", point)
            # Print total credit hours, total grade point here
            print("Total credit hours is ", total_credit, "hours.")
            print("Total grade point is ", totalGradePoint, ".")

            # Determining the class based on the GPA calculated
            if 3.60 <= gpa <= 4.00:
                print("Class: First Class")
            elif 3.00 <= gpa <= 3.59:
                print("Class: Second Class(Upper)")
            elif 2.00 <= gpa <= 2.99:
                print("Class: Second Class(Lower)")
            elif 1.50 <= gpa <= 1.99:
                print("Class: Third Class")
            elif 1.00 <= gpa <= 1.49:
                print("Class: Pass")
            elif 0.00 <= gpa <= 0.99:
                print("Fail")
            else:
                print("Can't determine class.")
        else:
            print("Good bye then ;)")
    elif response.upper() == 'N':
        print("Seems you have made a mistake with your courses, kindly re-enter your courses again: \n")
        course_select()
    else:
        print("Please enter Y or N.")


except (ValueError, NameError):
    print("You have entered an invalid input.")
