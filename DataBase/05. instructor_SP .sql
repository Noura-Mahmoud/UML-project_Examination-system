
---------------------------------------addQuestion---------------------------------------
create proc addQuestion @questionBody varchar(200), @crsID int, @choiceA nvarchar(50), @choiceB nvarchar(50), @choiceC nvarchar(50), @choiceD nvarchar(50),@correctAns nvarchar(50) WITH ENCRYPTION
as
BEGIN
	insert into Question (question, crsID) values(@questionBody, @crsID)

	declare @quesID nvarchar(200)
	select @quesID = quesID from Question where question = @questionBody
	insert into Choices (A, B, C, D, correctAnswer, quesID) values (@choiceA, @choiceB, @choiceC, @choiceD, @correctAns, @quesID)
END


----------------------------------------------------generateExam-----------------------------------------------

create or alter proc generateExam
	@crsID int,
	@nubOfQues int,
	@ExamDescription varchar(50),
	@ExamDurationMinutes int
	
WITH ENCRYPTION

as
--1
	insert into Exam(crsID,ExamDescription,ExamDurationMinutes) values(@crsID,@ExamDescription,@ExamDurationMinutes)
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

--------------------------------------------------------------------------
--if user exists the funcions return his ID otherwise returns 0

create or alter proc check_student @userName varchar(50), @password varchar(50) WITH ENCRYPTION
as
IF Exists (Select * from student s where s.username = @userName and s.password= @password)
Select s.stdID from student s where s.username = @userName and s.password= @password
ELSE
select 0
--=========================================================================

create or alter proc check_instructor @userName varchar(50), @password varchar(50) WITH ENCRYPTION
as
IF Exists (Select * from instructor i where i.username = @userName and i.password= @password)
Select i.insID from instructor i where i.username = @userName and i.password= @password
ELSE
select 0
--=========================================================================

create or alter proc check_admin @userName varchar(50), @password varchar(50) WITH ENCRYPTION
as
IF Exists (Select * from Admin a where a.username = @userName and a.password= @password)
Select a.adminID from Admin a where a.username = @userName and a.password= @password
ELSE
select 0





--testing


	 select*from Question
	 select * from Choices

	--run 
	exec generateExam 1,1
	

	--truncate table Exam
	delete from Exam
	delete from exam_question
	delete from Choices
	delete from Question