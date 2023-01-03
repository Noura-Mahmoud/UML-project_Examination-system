--instructor class functions 


CREATE DATABASE ExaminationSystem;

USE ExaminationSystem;

CREATE TABLE student 
(
stdID int IDENTITY(1,1),
FirstName varchar(50),
LastName varchar(50),

PRIMARY KEY (stdID)
);


CREATE TABLE instructor 
(
insID int IDENTITY(1,1),
FirstName varchar(50),
LastName varchar(50),

PRIMARY KEY (insID)
);


CREATE TABLE Admin 
(
adminID int IDENTITY(1,1),
FirstName varchar(50),
LastName varchar(50),
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

select * from student

INSERT INTO student (FirstName,LastName) VALUES ('ahmed', 'khaled');


----------------------------------------functions-----------------------------------------

---------------------------------------addQuestion---------------------------------------

create proc addQuestion @questionBody varchar(200), @crsID int, @choiceA nvarchar(50), @choiceB nvarchar(50), @choiceC nvarchar(50), @choiceD nvarchar(50),@correctAns nvarchar(50) WITH ENCRYPTION
as
	insert into Question (question, crsID) values(@questionBody, @crsID)

	declare @quesID nvarchar(200)
	select @quesID = quesID from Question where question = @questionBody
	insert into Choices (A, B, C, D, correctAnswer, quesID) values (@choiceA, @choiceB, @choiceC, @choiceD, @correctAns, @quesID)

	--use Examination_System
--run 
insert into instructor values('ahmed', 'mostafa')
insert into course (CrsName, insID) values('geo', 1)

 select*from Question
 select * from Choices

----------------------------------------------------generateExam-----------------------------------------------
	--DECLARE @quesTable TABLE(questionID int)
	declare @id int

create or alter proc generateExam @crsID int, @nubOfQues int WITH ENCRYPTION
as
--1
	insert into Exam(crsID) values(@crsID)
	--decalre temp table to questions and itereate on it by the cursor
	DECLARE @quesTable TABLE (questionID int)
--2
	INSERT INTO @quesTable select top (@nubOfQues) quesID from Question where crsID = @crsID order by newid() 

	--using cursor to loop over questions
	declare c1 cursor 
	for select * from @quesTable
	for read only

	declare @examID nvarchar(200)
	set @examID = (select TOP 1 ExamID FROM Exam order by ExamID desc)
	--set @id = @examID

	declare @qID int
	open c1
	fetch c1 into @qID
	while @@FETCH_STATUS=0
		begin
		--3
			insert into exam_question(examID, quesID) values(@examID, @qID)
			fetch c1 into @qID
		end
		select @examID
	close c1
	deallocate c1

	--run 
	exec generateExam 1,1
	

	--truncate table Exam
	delete from Exam
	delete from exam_question
	delete from Choices
	delete from Question
----------------------------------------------
