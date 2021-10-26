DROP DATABASE IF EXISTS COLLEGE_MANAGEMENT_SYSTEM;

CREATE DATABASE COLLEGE_MANAGEMENT_SYSTEM;

USE COLLEGE_MANAGEMENT_SYSTEM;

CREATE TABLE Student (
    StudentID int UNSIGNED AUTO_INCREMENT,
    FirstName varchar(50) NOT NULL CHECK(FirstName REGEXP '^[A-Za-z ]+$'),
    LastName varchar(50) CHECK(LastName REGEXP '^[A-Za-z ]+$'),
    Year int UNSIGNED NOT NULL CHECK(
        YEAR >= 1
        AND YEAR <= 12
    ),
    StreamName varchar(3) NOT NULL CHECK(
        StreamName IN ('CSD', 'CSE', 'ECE', 'ECD', 'CND', 'CHD', 'CLD')
    ),
    Address varchar(500) NOT NULL,
    Aadhaar BIGINT UNSIGNED NOT NULL CHECK(
        Aadhaar >= 100000000000
        and Aadhaar <= 999999999999
    ),
    NumberOfCourses int UNSIGNED NOT NULL,
    -- derived
    DOB date NOT NULL CHECK(DATEDIFF(DOB, '1990-01-01') >= 0),
    EnrollmentDate date NOT NULL,
    House varchar(6) CHECK(HOUSE IN ('blue', 'red', 'green', 'yellow')),
    PRIMARY KEY(StudentID)
);

CREATE TABLE Course (
    CourseID varchar(6) , 
    Credits int UNSIGNED,
    PRIMARY KEY(CourseID)
);

CREATE TABLE Guardian (
    FirstName varchar(50) NOT NULL,
    LastName varchar(50),
    StudentID int UNSIGNED NOT NULL,
    Address varchar(500) NOT NULL,
    CountryCode int UNSIGNED NOT NULL DEFAULT 91,
    PhoneNumber BIGINT UNSIGNED NOT NULL,
    EmailID varchar(255) NOT NULL CHECK(INSTR(EmailID, '@') > 0),
    FOREIGN KEY (StudentID) REFERENCES Student (StudentID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(FirstName, LastName, StudentID)
    
);

CREATE TABLE StudentAge (
    StudentID int UNSIGNED NOT NULL,
    DOB date NOT NULL,
    Age int UNSIGNED NOT NULL,
    FOREIGN KEY (StudentID) REFERENCES Student (StudentID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(StudentID)
);

CREATE TABLE StudentContactNumber (
    StudentID int UNSIGNED,
    CountryCode int UNSIGNED DEFAULT 91,
    PhoneNumber BIGINT UNSIGNED,
    FOREIGN KEY (StudentID) REFERENCES Student (StudentID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(StudentID, CountryCode, PhoneNumber)
);

CREATE TABLE StudentEmailID (
    StudentID int UNSIGNED,
    EmailID varchar(255) CHECK(INSTR(EmailID, '@') > 0),
    FOREIGN KEY (StudentID) REFERENCES Student (StudentID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(StudentID, EmailID)
);

CREATE TABLE Student_MedicalConditions (
    StudentID int UNSIGNED,
    MedicalConditions varchar(500) CHECK(MedicalConditions REGEXP '^[A-Za-z0-9 ]+$'),
    FOREIGN KEY (StudentID) REFERENCES Student (StudentID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(StudentID, MedicalConditions)
);

CREATE TABLE Student_Emergency (
    StudentID int UNSIGNED,
    Name varchar(100) CHECK(Name REGEXP '^[A-Za-z ]+$'),
    CountryCode int UNSIGNED NOT NULL DEFAULT 91,
    PhoneNumber BIGINT UNSIGNED NOT NULL,
    FOREIGN KEY (StudentID) REFERENCES Student (StudentID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(StudentID, Name)
);

CREATE TABLE Student_Courses (
    StudentID int UNSIGNED,
    CoursesStudyingID varchar(6) ,
    -- check if in Course table
    FOREIGN KEY (StudentID) REFERENCES Student (StudentID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (CoursesStudyingID) REFERENCES Course (CourseID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(StudentID, CoursesStudyingID)
);

CREATE TABLE Staff (
    StaffID int UNSIGNED AUTO_INCREMENT,
    FirstName varchar(50) NOT NULL CHECK(FirstName REGEXP '^[A-Za-z ]+$'),
    LastName varchar(50) CHECK(LastName REGEXP '^[A-Za-z ]+$'),
    Salary DOUBLE(10, 2) NOT NULL,
    BankAccountNumber BIGINT NOT NULL CHECK(BankAccountNumber < POWER(10, 16)),
    Aadhaar BIGINT UNSIGNED NOT NULL CHECK(
        Aadhaar >= 100000000000
        and Aadhaar <= 999999999999
    ),
    Address varchar(500) NOT NULL,
    DOB date NOT NULL CHECK(DATEDIFF(DOB, '1900-01-01') >= 0),
    JoiningDate date NOT NULL,
    PermanencyStatus varchar(15) CHECK(PermanencyStatus IN ('permanent', 'temporary')),
    PRIMARY KEY(StaffID)
);

CREATE TABLE StaffAge (
    StaffID int UNSIGNED,
    DOB date NOT NULL,
    Age int UNSIGNED NOT NULL,
    FOREIGN KEY (StaffID) REFERENCES Staff (StaffID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(StaffID)
);

CREATE TABLE StaffContactNumber (
    StaffID int UNSIGNED,
    CountryCode int UNSIGNED DEFAULT 91,
    PhoneNumber BIGINT UNSIGNED,
    FOREIGN KEY (StaffID) REFERENCES Staff (StaffID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(StaffID, CountryCode, PhoneNumber)
);

CREATE TABLE StaffEmailID (
    StaffID int UNSIGNED,
    EmailID varchar(255) CHECK(INSTR(EmailID, '@') > 0),
    FOREIGN KEY (StaffID) REFERENCES Staff (StaffID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(StaffID, EmailID)
);

CREATE TABLE StaffDesignation (
    StaffID int UNSIGNED,
    Designation varchar(20) CHECK (
        Designation IN ('Teacher', 'Teaching Assistant', 'Support staff')
    ),
    -- at least one fellow must be 'admin'
    FOREIGN KEY (StaffID) REFERENCES Staff (StaffID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(StaffID, Designation)
);

CREATE TABLE StaffMedicalConditions (
    StaffID int UNSIGNED,
    MedicalConditions varchar(500) CHECK(MedicalConditions REGEXP '^[A-Za-z0-9 ]+$'),
    FOREIGN KEY (StaffID) REFERENCES Staff (StaffID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(StaffID, MedicalConditions)
);

CREATE TABLE Staff_Qualifications (
    StaffID int UNSIGNED,
    Qualifications varchar(500) CHECK(Qualifications REGEXP '^[A-Za-z0-9 ,]+$'),
    FOREIGN KEY (StaffID) REFERENCES Staff (StaffID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(StaffID, Qualifications)
);

CREATE TABLE Teacher (
    StaffID int UNSIGNED,
    CoursesTeachingID varchar(6) ,
    -- check
    FOREIGN KEY (StaffID) REFERENCES Staff (StaffID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (CoursesTeachingID) REFERENCES Course (CourseID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(StaffID, CoursesTeachingID)
);

CREATE TABLE TeachingAssistant (
    StaffID int UNSIGNED,
    -- check
    StudentID int UNSIGNED,
    -- check
    CourseID varchar(6) ,
    -- check
    FOREIGN KEY (StudentID) REFERENCES Student (StudentID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (StaffID) REFERENCES Staff (StaffID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (CourseID) REFERENCES Course (CourseID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(StaffID, StudentID, CourseID)
);

CREATE TABLE Classroom (
    ClassroomID int CHECK(
        ClassroomID >= 10000
        AND ClassroomID < 100000
    ),
    BuildingName varchar(50) NOT NULL,
    -- check
    PRIMARY KEY(ClassroomID)
);

CREATE TABLE CoursesInClassroom (
    ClassroomID int ,
    CourseID varchar(6) ,
    -- check
    FOREIGN KEY (CourseID) REFERENCES Course (CourseID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (ClassroomID) REFERENCES Classroom (ClassroomID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(ClassroomID, CourseID)
);

CREATE TABLE Department (
    DepartmentID int CHECK (
        DepartmentID >= 1000
        AND DepartmentID <= 9999
    ),
    Name varchar(100) NOT NULL,
    HOD_ID int UNSIGNED NOT NULL,
    FOREIGN KEY (HOD_ID) REFERENCES Staff (StaffID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    -- CHECK THAT STAFF ID EXISTS
    PRIMARY KEY(DepartmentID)
);

CREATE TABLE WorksForDepartment (
    DepartmentID int,
    -- CHECK IN Department
    StaffID int UNSIGNED,
    FOREIGN KEY (StaffID) REFERENCES Staff (StaffID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    -- check in Staff
    FOREIGN KEY (DepartmentID) REFERENCES Department (DepartmentID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(DepartmentID, StaffID)
);

CREATE TABLE StudiesInDepartment (
    DepartmentID int,
    -- check
    StudentID int UNSIGNED,
    -- check
    FOREIGN KEY (StudentID) REFERENCES Student (StudentID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (DepartmentID) REFERENCES Department (DepartmentID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(DepartmentID, StudentID)
);



CREATE TABLE CoursePrerequisites (
    CourseID varchar(6) ,
    -- check
    Prerequisites varchar(6) ,
    -- CHECK IF EXISTS AS CourseID in Course
    FOREIGN KEY (CourseID) REFERENCES Course (CourseID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (Prerequisites) REFERENCES Course (CourseID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(CourseID, Prerequisites)
);

CREATE TABLE Dependent (
    StaffID int UNSIGNED,
    -- CHECK
    FirstName varchar(50) NOT NULL CHECK(FirstName REGEXP '^[A-Za-z ]+$'),
    LastName varchar(50) CHECK(LastName REGEXP '^[A-Za-z ]+$'),
    CountryCode int UNSIGNED DEFAULT 91,
    PhoneNumber BIGINT UNSIGNED,
    EmailID varchar(255) CHECK(INSTR(EmailID, '@') > 0),
    Address varchar(500) NOT NULL,
    FOREIGN KEY (StaffID) REFERENCES Staff (StaffID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(StaffID, FirstName, LastName)
);

CREATE TABLE Grade (
    Grade DOUBLE(4, 2) CHECK (
        Grade <= 10
        AND GRADE >= 0
    ),
    CourseID varchar(6) ,
    -- CHECK
    StudentID int UNSIGNED,
    -- check
    FOREIGN KEY (StudentID) REFERENCES Student (StudentID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (CourseID) REFERENCES Course (CourseID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(CourseID, StudentID)
);

CREATE TABLE Teaches (
    StudentID int UNSIGNED,
    -- check
    StaffID int UNSIGNED,
    -- check
    FOREIGN KEY (StudentID) REFERENCES Student (StudentID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (StaffID) REFERENCES Staff (StaffID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(StudentID, StaffID)
);

-- CREATE TABLE Enrolled (
--     StudentID int UNSIGNED,
--     -- check
--     CourseID varchar(6),
--     -- check
--     PRIMARY KEY(StudentID, CourseID)
-- );

CREATE TABLE Partof (
    TeacherHOD_ID int UNSIGNED,
    -- check
    TeacherMember_ID int UNSIGNED,
    -- check
    DepartmentID int,
    -- check
    FOREIGN KEY (TeacherHOD_ID) REFERENCES Staff (StaffID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (TeacherMember_ID) REFERENCES Staff (StaffID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (DepartmentID) REFERENCES Department (DepartmentID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(TeacherHOD_ID, TeacherMember_ID, DepartmentID)
);

CREATE TABLE MentorAStudent (
    StudentID int UNSIGNED,
    -- CHECK
    TeacherID int UNSIGNED,
    -- check
    DepartmentID int,
    -- check
    FOREIGN KEY (StudentID) REFERENCES Student (StudentID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (TeacherID) REFERENCES Staff (StaffID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (DepartmentID) REFERENCES Department (DepartmentID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(StudentID, TeacherID, DepartmentID)
);

CREATE TABLE Lecture (
    StudentID int UNSIGNED,
    -- check
    TeacherID int UNSIGNED,
    -- check
    CourseID varchar(6) ,
    -- check
    ClassroomID int ,
    -- check
    FOREIGN KEY (StudentID) REFERENCES Student (StudentID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (TeacherID) REFERENCES Staff (StaffID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (CourseID) REFERENCES Course (CourseID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (ClassroomID) REFERENCES Classroom (ClassroomID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(StudentID, TeacherID, CourseID, ClassroomID)
);

CREATE TABLE InvolvedInACourse (
    StudentID int UNSIGNED,
    -- check
    TeacherID int UNSIGNED,
    -- check
    CourseID varchar(6) ,
    -- check
    TeachingAssistantStaffID int UNSIGNED,
    -- check
    FOREIGN KEY (StudentID) REFERENCES Student (StudentID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (TeacherID) REFERENCES Staff (StaffID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (CourseID) REFERENCES Course (CourseID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    FOREIGN KEY (TeachingAssistantStaffID) REFERENCES Staff (StaffID)
    ON DELETE CASCADE ON UPDATE CASCADE ,
    PRIMARY KEY(
        StudentID,
        TeacherID,
        CourseID,
        TeachingAssistantStaffID
    )
);

DELIMITER //
CREATE TRIGGER StudentInsert
AFTER
INSERT
    ON Student FOR EACH ROW BEGIN
INSERT INTO
    StudentAge
VALUES
    (
        NEW.StudentID,
        NEW.DOB,
        YEAR(NOW()) - YEAR(NEW.DOB) - (
            DATE_FORMAT(NEW.DOB, '%m%d') < DATE_FORMAT(NOW(), '%m%d')
        )
    );

END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER StudentUpdate
AFTER
UPDATE
    ON Student FOR EACH ROW BEGIN
UPDATE
    StudentAge
SET
    Age = (
        YEAR(NOW()) - YEAR(NEW.DOB) - (
            DATE_FORMAT(NEW.DOB, '%m%d') < DATE_FORMAT(NOW(), '%m%d')
        )
    ),
    DOB = NEW.DOB
WHERE
    StudentID = NEW.StudentID;

END //
DELIMITER ;

-- DELIMITER //
-- CREATE TRIGGER StudentDelete
-- AFTER
--     DELETE ON Student FOR EACH ROW BEGIN
-- DELETE FROM
--     StudentAge
-- WHERE
--     StudentID = OLD.StudentID;

-- DELETE FROM
--     StudentContactNumber
-- WHERE
--     StudentID = OLD.StudentID;

-- DELETE FROM
--     StudentEmailID
-- WHERE
--     StudentID = OLD.StudentID;

-- DELETE FROM
--     Student_MedicalConditions
-- WHERE
--     StudentID = OLD.StudentID;

-- DELETE FROM
--     Student_Emergency
-- WHERE
--     StudentID = OLD.StudentID;

-- DELETE FROM
--     Student_Courses
-- WHERE
--     StudentID = OLD.StudentID;

-- DELETE FROM
--     TeachingAssistant
-- WHERE
--     StudentID = OLD.StudentID;

-- DELETE FROM
--     StudiesInDepartment
-- WHERE
--     StudentID = OLD.StudentID;

-- -- DELETE FROM
-- --     Guardian
-- -- WHERE
-- --     StudentID = OLD.StudentID;

-- DELETE FROM
--     Grade
-- WHERE
--     StudentID = OLD.StudentID;

-- DELETE FROM
--     Teaches
-- WHERE
--     StudentID = OLD.StudentID;

-- -- DELETE FROM
-- --     Enrolled
-- -- WHERE
-- --     StudentID = OLD.StudentID;

-- DELETE FROM
--     MentorAStudent
-- WHERE
--     StudentID = OLD.StudentID;

-- DELETE FROM
--     Lecture
-- WHERE
--     StudentID = OLD.StudentID;

-- DELETE FROM
--     InvolvedInACourse
-- WHERE
--     StudentID = OLD.StudentID;

-- END //
-- DELIMITER ;

DELIMITER //
CREATE TRIGGER StaffInsert
AFTER
INSERT
    ON Staff FOR EACH ROW BEGIN
INSERT INTO
    StaffAge
VALUES
    (
        NEW.StaffID,
        NEW.DOB,
        YEAR(NOW()) - YEAR(NEW.DOB) - (
            DATE_FORMAT(NEW.DOB, '%m%d') < DATE_FORMAT(NOW(), '%m%d')
        )
    );

END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER StaffUpdate
AFTER
UPDATE
    ON Staff FOR EACH ROW BEGIN
UPDATE
    StaffAge
SET
    Age = (
        YEAR(NOW()) - YEAR(NEW.DOB) - (
            DATE_FORMAT(NEW.DOB, '%m%d') < DATE_FORMAT(NOW(), '%m%d')
        )
    ),
    DOB = NEW.DOB
WHERE
    StaffID = NEW.StaffID;

END //
DELIMITER ;

-- DELIMITER //
-- CREATE TRIGGER StaffDelete
-- AFTER
--     DELETE ON Staff FOR EACH ROW BEGIN
-- DELETE FROM
--     StaffAge
-- WHERE
--     StaffID = OLD.StaffID;

-- DELETE FROM
--     StaffContactNumber
-- WHERE
--     StaffID = OLD.StaffID;

-- DELETE FROM
--     StaffEmailID
-- WHERE
--     StaffID = OLD.StaffID;

-- DELETE FROM
--     StaffDesignation
-- WHERE
--     StaffID = OLD.StaffID;

-- DELETE FROM
--     StaffMedicalConditions
-- WHERE
--     StaffID = OLD.StaffID;

-- DELETE FROM
--     Staff_Qualifications
-- WHERE
--     StaffID = OLD.StaffID;

-- DELETE FROM
--     Teacher
-- WHERE
--     StaffID = OLD.StaffID;

-- DELETE FROM
--     TeachingAssistant
-- WHERE
--     StaffID = OLD.StaffID;

-- DELETE FROM
--     WorksForDepartment
-- WHERE
--     StaffID = OLD.StaffID;

-- DELETE FROM
--     Dependent
-- WHERE
--     StaffID = OLD.StaffID;

-- DELETE FROM
--     Teaches
-- WHERE
--     StaffID = OLD.StaffID;

-- DELETE FROM
--     Partof
-- WHERE
--     TeacherHOD_ID = OLD.StaffID
--     OR TeacherMember_ID = OLD.StaffID;

-- DELETE FROM
--     MentorAStudent
-- WHERE
--     TeacherID = OLD.StaffID;

-- DELETE FROM
--     Lecture
-- WHERE
--     TeacherID = OLD.StaffID;

-- DELETE FROM
--     InvolvedInACourse
-- WHERE
--     TeacherID = OLD.StaffID
--     OR TeachingAssistantStaffID = OLD.StaffID;

-- END //
-- DELIMITER ;

-- DELIMITER //
-- CREATE TRIGGER TeacherInsert
-- BEFORE
--     INSERT ON Teacher FOR EACH ROW BEGIN
-- DECLARE myvar BIGINT;
-- -- DECLARE this_staff_id BIGINT;
-- SELECT NEW.StaffID INTO @this_staff_id;
-- \! echo 'some text';
-- SELECT COUNT(*) INTO myvar FROM Staff WHERE StaffID = this_staff_id;
-- IF ((myvar) = 0) THEN
--     signal sqlstate '45000' set message_text = 'Error: No Staff Found With That StaffID';
-- -- ELSEIF CoursesTeachingID NOT IN (SELECT CourseID FROM Course) THEN
-- --     signal sqlstate '45000' set message_text = 'Error: No Course Found With That CourseID';
-- END IF;

-- -- IF StaffID NOT IN (SELECT StaffID FROM Staff) THEN
-- --     signal sqlstate '45000' set message_text = 'Error: No Staff Found With That StaffID';
-- -- ELSEIF CoursesTeachingID NOT IN (SELECT CourseID FROM Course) THEN
-- --     signal sqlstate '45000' set message_text = 'Error: No Course Found With That CourseID';
-- -- END IF;
-- END //
-- DELIMITER ;


/* Student */
INSERT INTO
    Student
values
    (
        NULL,
        'Aaron',
        'Monis',
        2,
        'CSE',
        '23 Dasa Road, Dubai',
        845213659875,
        2,
        '2002-01-20',
        '2020-07-20',
        'blue'
    );

INSERT INTO
    Student
values
    (
        NULL,
        'Aditya',
        'Harikrish',
        2,
        'CSD',
        '12 SV Road, Mumbai',
        961465789645,
        2,
        '2002-12-21',
        '2020-08-20',
        'red'
    );

INSERT INTO
    Student
values
    (
        NULL,
        'Krishna',
        'Praneet',
        2,
        'CND',
        'Dammaiguda, Hyderabad',
        789653215789,
        2,
        '2002-08-04',
        '2020-08-17',
        'blue'
    );
INSERT INTO
    Staff
VALUES
    (
        NULL,
        'Radha',
        'Reddy',
        50000.0,
        8452136598754567,
        845213659875,
        'Gachibowli, Hyderabad',
        '1980-07-17',
        '2000-06-01',
        'permanent'
    );

INSERT INTO
    Staff
VALUES
    (
        NULL,
        'BG',
        'Garg',
        90000.0,
        5642317894567891,
        456798365147,
        'Santacruz West, Mumbai',
        '1970-09-14',
        '1996-12-08',
        'permanent'
    );

INSERT INTO
    Staff
VALUES
    (
        NULL,
        'Siddant',
        'Malhotra',
        95000.0,
        7894556423167891,
        458967893214,
        'Dharavi, Mumbai',
        '1975-02-01',
        '2005-11-29',
        'temporary'
    );

INSERT INTO
    Staff
VALUES
    (
        NULL,
        'Aaron',
        'Monis',
        2000.0,
        4589317856421789,
        845213659875,
        '23 Dasa Road, Dubai',
        '2002-01-20',
        '2021-07-31',
        'temporary'
    );

INSERT INTO
    Course
VALUES
    ('CS01.3', 2);

INSERT INTO
    Course
VALUES
    ('ISS1.3', 2);

INSERT INTO
    Course
VALUES
    ('DSA1.3', 2);

INSERT INTO
    Classroom
VALUES
    (10001,'GyanBhavan');

INSERT INTO
    Department
VALUES
    (1001,'Science Department',2);



INSERT INTO
    StudentContactNumber
VALUES
(1, 91, 9874563651);

INSERT INTO
    StudentContactNumber
VALUES
(2, 91, 9579963602);

INSERT INTO
    StudentContactNumber
VALUES
(3, 91, 8764563612);
-- 
INSERT INTO
    StudentEmailID
VALUES
(1, 'mybigbishop@hotmail.com');

INSERT INTO
    StudentEmailID
VALUES
(2, 'badassadi@gmail.com');

INSERT INTO
    StudentEmailID
VALUES
(3, 'pranilucifer@hotmail.com');
-- 
INSERT INTO
    Student_MedicalConditions
VALUES
    (1, 'Asthma');

INSERT INTO
    Student_Emergency
VALUES
    (1, 'Priya Rani', 91, 4456789234);

INSERT INTO
    Student_Emergency
VALUES
    (2, 'Rahul Tewatia', 91, 6908374212);

INSERT INTO
    Student_Emergency
VALUES
    (1, 'Aamuktamalyada', 91, 9082917462);

INSERT INTO
    Student_Courses
VALUES
    (1, 'CS01.3');

INSERT INTO
    Student_Courses
VALUES
    (1, 'DSA1.3');

INSERT INTO
    Student_Courses
VALUES
    (2, 'DSA1.3');

INSERT INTO
    Student_Courses
VALUES
    (2, 'ISS1.3');

INSERT INTO
    Student_Courses
VALUES
    (3, 'CS01.3');

INSERT INTO
    Student_Courses
VALUES
    (3, 'ISS1.3');

/* Guardian */
INSERT INTO
    Guardian
VALUES
    (
        'Rohan',
        'C',
        3,
        '13 Beth Street, New York',
        91,
        7894652315,
        "rohan@gmail.com"
    );

INSERT INTO
    Guardian
VALUES
    (
        'Maria',
        'D''Souza',
        1,
        '221B Baker Street, London',
        44,
        2072243688,
        "elementaryMyDearWatson@gmail.com"
    );

INSERT INTO
    Guardian
VALUES
    (
        'Shylock',
        'FleshLess',
        1,
        'Platform 9 3/4, King''s Cross Station, London',
        44,
        2078331137,
        "AvadaKedavra@gmail.com"
    );



INSERT INTO
    StaffContactNumber
VALUES
(1, 91, 9473829561);

INSERT INTO
    StaffContactNumber
VALUES
(2, 91, 9473837719);

INSERT INTO
    StaffContactNumber
VALUES
(3, 91, 8673829599);

INSERT INTO
    StaffEmailID
VALUES
(1, 'mymail@hotmail.com');

INSERT INTO
    StaffEmailID
VALUES
(2, 'dryrun@gmail.com');

INSERT INTO
    StaffEmailID
VALUES
(3, 'zindabad@hotmail.com');
-- 
INSERT INTO
    StaffDesignation
VALUES
(1, 'Support staff');

INSERT INTO
    StaffDesignation
VALUES
(2, 'Teacher');

INSERT INTO
    StaffDesignation
VALUES
(3, 'Teacher');

INSERT INTO
    StaffDesignation
VALUES
(4, 'Teaching Assistant');

INSERT INTO
    StaffMedicalConditions
VALUES
    (3, 'Arthiritis');

INSERT INTO
    StaffMedicalConditions
VALUES
    (2, 'Hypertension');

INSERT INTO
    Staff_Qualifications
VALUES
    (1, 'MBA');

INSERT INTO
    Staff_Qualifications
VALUES
    (2, 'BSc , BEd');

INSERT INTO
    Staff_Qualifications
VALUES
    (3, 'BSc , MSc in Natural Sciences');

INSERT INTO
    Teacher
VALUES
    (2,'CS01.3');

INSERT INTO
    Teacher
VALUES
    (3,'DSA1.3');

INSERT INTO
    Teacher
VALUES
    (3,'ISS1.3');

INSERT INTO
    TeachingAssistant
VALUES
    (4, 1, "ISS1.3");



INSERT INTO
    CoursesInClassroom
VALUES
    (10001,'DSA1.3');

INSERT INTO
    CoursesInClassroom
VALUES
    (10001,'ISS1.3');

INSERT INTO
    CoursesInClassroom
VALUES
    (10001,'CS01.3');



INSERT INTO
    WorksForDepartment
VALUES
    (1001,2);

INSERT INTO
    WorksForDepartment
VALUES
    (1001,3);

INSERT INTO
    StudiesInDepartment
VALUES
    (1001,3);



INSERT INTO
    CoursePrerequisites
VALUES
    ('ISS1.3', 'DSA1.3');

INSERT INTO
    Dependent
VALUES
    (
        1,
        'Murali',
        'Krishna',
        91,
        9002341137,
        "murali@gmail.com",
        "Medak, Telangana"
    );

INSERT INTO
    Dependent
VALUES
    (
        2,
        'Jaya',
        'Durga',
        91,
        9674911939,
        "jayadurga@gmail.com",
        "Kolkata, West Bengal"
    );

INSERT INTO
    Grade
VALUES
    (9.7,'CS01.3', 2);

INSERT INTO
    Grade
VALUES
    (9.3,'CS01.3', 1);

INSERT INTO
    Grade
VALUES
    (9.5,'CS01.3', 3);

INSERT INTO Teaches (StudentID,StaffID)
SELECT DISTINCT Student_Courses.StudentID , Teacher.StaffID
FROM Student_Courses
INNER JOIN Teacher
ON Student_Courses.CoursesStudyingID = Teacher.CoursesTeachingID;

INSERT INTO Partof (TeacherHOD_ID,TeacherMember_ID,DepartmentID)
SELECT DISTINCT Department.HOD_ID,WorksForDepartment.StaffID,Department.DepartmentID
FROM Department
LEFT JOIN WorksForDepartment
ON Department.DepartmentID = WorksForDepartment.DepartmentID;

INSERT INTO MentorAStudent (StudentID,TeacherID,DepartmentID)
SELECT DISTINCT StudiesInDepartment.StudentID,WorksForDepartment.StaffID,StudiesInDepartment.DepartmentID
FROM StudiesInDepartment
LEFT JOIN WorksForDepartment
ON StudiesInDepartment.DepartmentID = WorksForDepartment.DepartmentID;


INSERT INTO Lecture (StudentID,TeacherID,CourseID,ClassroomID)
SELECT DISTINCT Student_Courses.StudentID,Teacher.StaffID, Student_Courses.CoursesStudyingID, CoursesInClassroom.ClassroomID
FROM Student_Courses
LEFT JOIN Teacher
ON Student_Courses.CoursesStudyingID = Teacher.CoursesTeachingID
LEFT JOIN CoursesInClassroom
ON Student_Courses.CoursesStudyingID = CoursesInClassroom.CourseID;

INSERT INTO InvolvedInACourse (StudentID,TeacherID,CourseID,TeachingAssistantStaffID)
SELECT DISTINCT Student_Courses.StudentID,Teacher.StaffID, Student_Courses.CoursesStudyingID, TeachingAssistant.StaffID
FROM Student_Courses
LEFT JOIN Teacher
ON Student_Courses.CoursesStudyingID = Teacher.CoursesTeachingID
LEFT JOIN TeachingAssistant
ON Student_Courses.CoursesStudyingID = TeachingAssistant.CourseID
WHERE TeachingAssistant.StaffID IS NOT NULL;

