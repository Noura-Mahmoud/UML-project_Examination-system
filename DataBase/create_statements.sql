CREATE DATABASE ExaminationSystem;

USE ExaminationSystem;

CREATE TABLE student 
(
stdID int IDENTITY(1,1),
FirstName varchar(50),
LastName varchar(50),
username varchar(50),
password varchar(50),

PRIMARY KEY (stdID)
);


CREATE TABLE instructor 
(
insID int IDENTITY(1,1),
FirstName varchar(50),
LastName varchar(50),
username varchar(50),
password varchar(50),

PRIMARY KEY (insID)
);


CREATE TABLE Admin 
(
adminID int IDENTITY(1,1),
FirstName varchar(50),
LastName varchar(50),
username varchar(50),
password varchar(50),
PRIMARY KEY (adminID)
);

CREATE TABLE course 
(
crsID int IDENTITY(1,1),
CrsName varchar(50),
insID int,
PRIMARY KEY (crsID),
FOREIGN KEY (insID) REFERENCES instructor(insID)
);

CREATE TABLE std_course 
(
stdID int,
crsID int,
state varchar(10) DEFAULT 'pending',
PRIMARY KEY (stdID,crsID),
FOREIGN KEY (stdID) REFERENCES student(stdID),
FOREIGN KEY (crsID) REFERENCES course(crsID)
);

--alter table std_course add state varchar(10);

CREATE TABLE Exam
(
ExamID int PRIMARY KEY IDENTITY(1,1),
ExamDescription varchar(250),
ExamDurationMinutes int,
crsID int, 
FOREIGN KEY (crsID) REFERENCES course(crsID)
);

CREATE TABLE Question
(
quesID int IDENTITY(1,1),
question varchar(150),
crsID int,
PRIMARY KEY (quesID),
FOREIGN KEY (crsID) REFERENCES course(crsID)
);


CREATE TABLE Choices
(
ChoicesID int IDENTITY(1,1),
A varchar(50),
B varchar(50),
C varchar(50),
D varchar(50),
correctAnswer varchar(50),
quesID int,
PRIMARY KEY (ChoicesID),
FOREIGN KEY (quesID) REFERENCES question(quesID)
);

CREATE TABLE exam_question
(
examID int,
quesID int,
PRIMARY KEY (examID,quesID),
FOREIGN KEY (examID) REFERENCES exam(examID),
FOREIGN KEY (quesID) REFERENCES question(quesID)
);

CREATE TABLE student_exam
(
examID int,
stdID int,
grade decimal,
PRIMARY KEY (examID,stdID),
FOREIGN KEY (examID) REFERENCES exam(examID),
FOREIGN KEY (stdID) REFERENCES student(stdID)
);

CREATE TABLE std_answers
(
    stdID int,
    quesID int,
    answer varchar(50),
    PRIMARY KEY (stdID, quesID),
    FOREIGN KEY (stdID) REFERENCES student(stdID),
    FOREIGN KEY (quesID) REFERENCES question(quesID)
);

