CREATE DATABASE ExaminationSystem;
-- DROP DATABASE ExaminationSystem;
USE ExaminationSystem;

CREATE TABLE student 
(
stdID int,
FirstName varchar(50),
LastName varchar(50),

PRIMARY KEY (stdID)
);


CREATE TABLE instructor 
(
insID int,
FirstName varchar(50),
LastName varchar(50),

PRIMARY KEY (insID)
);


CREATE TABLE Admin 
(
adminID int,
FirstName varchar(50),
LastName varchar(50),
PRIMARY KEY (adminID)
);

CREATE TABLE course 
(
crsID int,
CrsName varchar(50),
insID int,
PRIMARY KEY (crsID),
FOREIGN KEY (insID) REFERENCES instructor(insID)
);

CREATE TABLE std_course 
(
stdID int,
crsID int,
PRIMARY KEY (stdID,crsID),
FOREIGN KEY (stdID) REFERENCES student(stdID),
FOREIGN KEY (crsID) REFERENCES course(crsID)
);

CREATE TABLE Exam
(
ExamID int PRIMARY KEY,
ExamDescription varchar(250),
ExamDurationMinutes int,
crsID int, 
FOREIGN KEY (crsID) REFERENCES course(crsID)
);

CREATE TABLE Question
(
quesID int,
question varchar(150),
crsID int,
PRIMARY KEY (quesID),
FOREIGN KEY (crsID) REFERENCES course(crsID)
);


CREATE TABLE Choices
(
ChoicesID int,
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