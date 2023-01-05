import admin, student, instructor, question, exam
from databaseConnector import  connector
conn = connector()

def check_student(userName,password):
    cursor = conn.cursor()
    cursor.execute("check_student ?,?;",(userName,password))
    for row in cursor:
        for val in row: 
            print(val)
            return val
        
def check_instructor(userName,password):
    cursor = conn.cursor()
    cursor.execute("check_instructor ?,?;",(userName,password))
    for row in cursor:
        for val in row: 
            print(val)
            return val
        
        
def check_admin(userName,password):
    cursor = conn.cursor()
    cursor.execute(" check_admin ?,?;",(userName,password))
    for row in cursor:
        for val in row: 
            print(val)
            return val
        
def initializing():
    option= int( input("wlecome to Examination-system\n-------------------------------\nTo log in press 1 \nTo sign up press 2\n"))
    option = int(option)
    if option == 1:
        loginMenu()
    elif option == 2: # in student table
        print("please enter your first name")
        fname = input()
        print("please enter your last name")
        lname = input()
        print("please enter your username")
        username = input()
        print("please enter your password")
        password = input()
        cursor = conn.cursor()
        cursor.execute(
        "insert into student(FirstName,LastName, username, password) values (?,?,?,?);",
         (fname,lname, username, password)   
        )
        conn.commit()
        
        loginMenu()

def loginMenu():
  type= int( input("wlecome to Examination-system\n-------------------------------\nchoose ur type to login\n1-Admin\n2-instructor\n3-Student\n") )
  while type>3 or type<1:
    type= int (input("invalid type please try again"))
    
    
  username=input("username:")
  password=input("userpassword:")
    
  if type == 1:
      check = check_admin(username,password)
      if check != 0:
        adminUser()
      else:
          print("\nplease try again\n")
          loginMenu()
    # adminUser()
  elif type == 2:
      check = check_instructor(username,password)
      if check != 0:
        instructorUser()
      else:
        print("\nplease try again\n")
        loginMenu()
  elif type == 3:
      stdID = check_student(username,password)
      if stdID != 0:
        studentUser(stdID)
      else:
        print("\nplease try again\n")
        loginMenu()

def studentUser(stdID):
    print("if you want to \nenroll new course press 1, \nget approved courses press 2, \ntake exam press 3, \nget your grades press 4\n")
    userFunction = int(input())
    # userFunction = input()
    st1=student.Student(stdID,"a")
    if userFunction == 1:
        print("please insert the course name")
        # crsID = input()
        crsName = input()
        st1.enroll(crsName)
        studentUser(stdID)
    elif userFunction == 2:
        st1.getCourses()
        studentUser(stdID)
    elif userFunction == 3:
        print("please insert the exam id")
        # examID = input()
        examID = int(input())
        st1.takeExam(examID)
        studentUser(stdID)
    elif userFunction==4:
        st1.getGrades()
        studentUser(stdID)
    else:
        print("please choose 1, 2, 3 or 4")

def adminUser():
    # userFunction = input()
    ad1= admin.Admin("a")
    flag= True

    while flag:
        print("PRESS 1:\n\tTo add new course, \nPRESS 2:\n\tTo edit course, \nPRESS 3:\n\tTo delete course, \nPRESS 4:\n\tinsert new instructor, \nPRESS 5:\n\tTo edit instructor. \nPRESS 6:\n\tTo delete instructor. \nPRESS 7:\n\tTo Approve courses \nPRESS 8:\n\tTo generate report.\nPRESS 0:\n\tTo LOGOUT")

        userFunction = int(input())
    
        if userFunction == 1:
            print("please insert the course name")
            courseName = input()
            print("please insert the instructor id associated to this course")
            insID = input()
            ad1.addCourse(courseName, insID)
        elif userFunction == 2:
            print("please insert the course name you want to change")
            old = input()
            print("please insert the new course name")
            new = input()
            ad1.editCourseName(old, new)
        elif userFunction == 3:
            print("please insert the course name")
            courseName = input()
            ad1.deleteCourse(courseName)
        elif userFunction == 4:
            print("please insert the instructor first name")
            InstructorFName = input()
            print("please insert the instructor last name")
            InstructorLName = input()
            print("please insert the instructor username")
            userName = input()
            print("please insert the instructor password")
            password = input()
            ins1 = instructor.Instrucor(InstructorFName, InstructorLName, userName, password)
            ad1.addInstructor(ins1.fname, ins1.lname, ins1.username, ins1.password)
        elif userFunction == 5:
            print("please insert the instructor id")
            InstructorID = input()
            print("please insert the instructor name")
            InstructorName = input()
            ad1.editInstructorUsername(InstructorID, InstructorName)
        elif userFunction == 6:
            print("please insert the instructor id")
            InstructorID = input()
            ad1.deleteInstructor(InstructorID)
        elif userFunction == 7:
            ad1.approveDeclineStudents()
        elif userFunction == 8:
            ad1.generateReport()
        elif userFunction == 0:
            flag = False
            loginMenu()
        else:
            print("please select a number from 1 to 8 or PRESS 0 to LOGOUT")
            adminUser()
   
def instructorUser():
    print("if you want to add new question press 1, \ngenerate exam press 2")
    # userFunction = input()
    userFunction = int(input())
    ins1 = instructor.Instrucor("a")
    if userFunction == 1:
        print("please enter the question body")
        questionBody = input()
        print("please enter the course id")
        crsID = input()
        print("please enter the choiceA")
        choiceA = input()
        print("please enter the choiceB")
        choiceB = input()
        print("please enter the choiceC")
        choiceC = input()
        print("please enter the choiceD")
        choiceD = input()
        print("please enter the correct answer")
        correctAns = input()
        ques = question.Question(questionBody, crsID, choiceA, choiceB, choiceC, choiceD, correctAns)
        ins1.addQuestion(ques)
        instructorUser()
    elif userFunction == 2:
        print("please enter the course id")
        # crsID = input()
        crsID = int(input())
        print("please enter the number of questions")
        NumOfQuestion = input()
        exam1 = exam.Exam(crsID, NumOfQuestion)
        ins1.generateExam(exam1)
        instructorUser()


initializing()
# loginMenu()
