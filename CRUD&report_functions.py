


import pyodbc
import pandas as pd

from prettytable import PrettyTable


def read(conn):
    print("read...")
    cursor = conn.cursor()
    cursor.execute("select * from student")
    for row in cursor:
        print(f'row = {row}')
        
    print()


def insert(conn,Sid,Fname,Lname):
    print("insert...")
    cursor = conn.cursor()
    cursor.execute(
        "insert into student(stdID,FirstName,LastName) values (?,?,?);",
         (Sid,Fname,Lname)
        )
    conn.commit()
    

#update first_name depend on id
def update(conn,Fname,Sid):
    print("update...")
    cursor = conn.cursor()
    cursor.execute(
        "update student set FirstName = ? where stdID = ?;",
         (Fname,Sid)
        )
    conn.commit()


#delete depend on id
def delete(conn,Sid):
    print("delete...")
    cursor = conn.cursor()
    cursor.execute(
        "delete from student where stdID = ?;",
         (Sid)
        )
    conn.commit()



#connec to database
conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=DESKTOP-IQ1O672\SQLEXPRESS;"
        "Database=ExaminationSystem;"
        "Trusted_Connection=yes;"
    )


read(conn)


update(conn,"hamada",2)



read(conn)





get_ipython().system('pip install prettytable')



from prettytable import PrettyTable


def highest_grade_each_studet_get(save_to_csv=False):
    sql_query = pd.read_sql_query(''' 
                              select [student name], grade
                                from( 
                                select s.FirstName+' '+s.LastName [student name], se.grade,
                                    dense_rank() over (partition by s.stdID order by se.grade desc ) as gradess
                                    from student s
                                    inner join student_exam se on s.stdID = se.stdID
                                    inner join Exam e on se.examID = e.ExamID

                                )t
                                where gradess =1
                                order by gradess asc
                              '''
                              ,conn) # here, the 'conn' is the variable that contains your database connection information from step 2

    df = pd.DataFrame(sql_query)
    if save_to_csv:
        df.to_csv(r'highest_grade_each_studet_get.csv', index=False)
    else:
        table = PrettyTable()
        table.field_names = ["Student Name", "Grade"]
        for index, row in df.iterrows():
            table.add_row([row["student name"], row["grade"]])
        print(table)



highest_grade_each_studet_get(True)



def highest_grade_each_course(save_to_csv=False):
    sql_query = pd.read_sql_query(''' 
                              select [student name], [course name], grade
                                from( 
                                select s.FirstName+' '+s.LastName [student name], c.CrsName [course name], se.grade,
                                    dense_rank() over (partition by c.CrsName order by se.grade desc ) as gradess
                                    from student s
                                    inner join student_exam se on s.stdID = se.stdID
                                    inner join Exam e on se.examID = e.ExamID
                                    inner join course c on e.crsID =c.crsID
                                )tmp
                                where gradess =1
                                order by gradess asc
                              '''
                              ,conn) # here, the 'conn' is the variable that contains your database connection information from step 2
    df = pd.DataFrame(sql_query)
    if save_to_csv:
        df.to_csv (r'highest_grade_at_each_course.csv', index = False) # place 'r' before the path name
    else:
        table = PrettyTable()
        table.field_names = ["Student Name", "course name","grade"]
        for index, row in df.iterrows():
            table.add_row([row["student name"],row["course name"], row["grade"]])
        print(table)



highest_grade_each_course(False)


def Num_students_at_each_course(save_to_csv=False):
    sql_query = pd.read_sql_query(''' 
                              select c.CrsName [course Name], count(*) [number of student] from student
                              s inner join std_course sc on s.stdID =sc.stdID inner join 
                              course c on sc.crsID = c.crsID group by(c.CrsName)
                              '''
                              ,conn) # here, the 'conn' is the variable that contains your database connection information from step 2

    df = pd.DataFrame(sql_query)
    if save_to_csv:
        df.to_csv (r'num_students_each_course.csv', index = False) # place 'r' before the path name
    else:
        table = PrettyTable()
        table.field_names = ["Student Name", "course name"]
        for index, row in df.iterrows():
            table.add_row([row["course Name"],row["number of student"]])
        print(table)



Num_students_at_each_course(False)



def all_students_data_report(save_to_csv=False):
    sql_query = pd.read_sql_query(''' 
                              select * from student
                              '''
                              ,conn) # here, the 'conn' is the variable that contains your database connection information from step 2

    df = pd.DataFrame(sql_query)
    if save_to_csv:
        df.to_csv (r'all_students_info.csv', index = False) # place 'r' before the path name
    else:
        table = PrettyTable()
        table.field_names = ["stdID","FirstName", "LastName"]
        for index, row in df.iterrows():
            table.add_row([row["stdID"],row["FirstName"],row["LastName"]])
        print(table)



all_students_data_report(True)


