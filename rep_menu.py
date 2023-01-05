import pyodbc
import pandas as pd

from databaseConnector import array_to_table, connector
from prettytable import PrettyTable

import warnings

warnings.filterwarnings('ignore')

conn = connector()


class reportClass:
    value =0
    save_to_csv =False
    def __init__(self):
        pass
        
    #all student raws
    
    def all_students_data_report(self,save_to_csv):
        save_to_csv= save_to_csv
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

        #number of student at each course
    
    def Num_students_at_each_course(self,save_to_csv):

        save_to_csv= save_to_csv
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


#name of studen who get the highest grade at each course 
    def highest_grade_each_course(self,save_to_csv):
        save_to_csv= save_to_csv
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

    #highest_grade_each_studet_get

    def highest_grade_each_studet_get(self,save_to_csv):

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
            
    def menu(self):
        value = int(input("choose report\n1)all student\n2)Number of student at each course\n3)highest score at each course\n4)highest grade each student get\n"))
        save_to_csv = int(input("print /CSV file:\nPRESS 0:\n\tto print table at console\nPRESS 1:\n\tget csv file\n"))
        print(save_to_csv)
        print(type(save_to_csv))
        if value==1:
            self.all_students_data_report(save_to_csv)
        elif value==2:
            self.Num_students_at_each_course(save_to_csv)
        elif value==3:
            self.highest_grade_each_course(save_to_csv)
        elif value==4:
            self.highest_grade_each_studet_get(save_to_csv)


