DROP DATABASE IF EXISTS COLLEGE_MANAGEMENT_SYSTEM;

CREATE DATABASE COLLEGE_MANAGEMENT_SYSTEM;

USE COLLEGE_MANAGEMENT_SYSTEM;

CREATE TABLE Student (
    StudentID int UNSIGNED AUTO_INCREMENT,
    FirstName varchar(50) NOT NULL CHECK(FirstName REGEXP '^[A-Za-z]+$'),
    LastName varchar(50) CHECK(LastName REGEXP '^[A-Za-z]+$'),
    Year int UNSIGNED NOT NULL CHECK(
        YEAR >= 1
        AND YEAR <= 12
    ),
    StreamName varchar(3) NOT NULL CHECK(
        StreamName IN ('CSD', 'CSE', 'ECE', 'ECD', 'CND', 'CHD', 'CLD')
    ),
    Address varchar(500) NOT NULL CHECK(Address REGEXP '^[A-Za-z0-9]+$'),
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

CREATE TABLE Guardian (
    FirstName varchar(50) NOT NULL,
    LastName varchar(50),
    StudentID int UNSIGNED NOT NULL,
    Address varchar(500) NOT NULL,
    CountryCode int UNSIGNED NOT NULL DEFAULT 91,
    PhoneNumber BIGINT UNSIGNED NOT NULL,
    EmailID varchar(255) NOT NULL CHECK(INSTR(EmailID, '@') > 0),
    PRIMARY KEY(FirstName, LastName, StudentID)
);

CREATE TABLE StudentAge (
    StudentID int UNSIGNED NOT NULL,
    DOB date NOT NULL,
    Age int unsigned NOT NULL,
    PRIMARY KEY(StudentID)
);

CREATE TABLE StudentContactNumber (
    StudentID int UNSIGNED,
    CountryCode int UNSIGNED DEFAULT 91,
    PhoneNumber BIGINT UNSIGNED,
    PRIMARY KEY(StudentID, CountryCode, PhoneNumber)
);

CREATE TABLE StudentEmailID (
    StudentID int UNSIGNED,
    EmailID varchar(255) CHECK(INSTR(EmailID, '@') > 0),
    PRIMARY KEY(StudentID, EmailID)
);

CREATE TABLE Student_MedicalConditions (
    StudentID int UNSIGNED,
    MedicalConditions varchar(500) CHECK(MedicalConditions REGEXP '^[A-Za-z0-9]+$'),
    PRIMARY KEY(StudentID, MedicalConditions)
);

CREATE TABLE Student_Emergency (
    StudentID int UNSIGNED,
    Name varchar(100) CHECK(Name REGEXP '^[A-Za-z]+$'),
    CountryCode int UNSIGNED NOT NULL DEFAULT 91,
    PhoneNumber BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY(StudentID, Name)
);

CREATE TABLE Student_Courses (
    StudentID int UNSIGNED,
    CoursesStudyingID varchar(6), -- check if in Course table
    PRIMARY KEY(StudentID, CoursesStudyingID)
);

CREATE TABLE Staff (
    StaffID int UNSIGNED AUTO_INCREMENT,
    FirstName varchar(50) NOT NULL,
    LastName varchar(50),
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
    Age int unsigned NOT NULL,
    PRIMARY KEY(StaffID)
);

CREATE TABLE StaffContactNumber (
    StaffID int UNSIGNED,
    CountryCode int UNSIGNED DEFAULT 91,
    PhoneNumber BIGINT UNSIGNED,
    PRIMARY KEY(StaffID, CountryCode, PhoneNumber)
);

CREATE TABLE StaffEmailID (
    StaffID int UNSIGNED,
    EmailID varchar(255) CHECK(INSTR(EmailID, '@') > 0),
    PRIMARY KEY(StaffID, EmailID)
);

CREATE TABLE StaffDesignation (
    StaffID int,
    Designation varchar(20), -- at least one fellow must be 'admin'
    PRIMARY KEY(StaffID, Designation)
);

CREATE TABLE StaffMedicalConditions (
    StaffID int,
    MedicalConditions varchar(500),
    PRIMARY KEY(StaffID, MedicalConditions)
);

CREATE TABLE Staff_Qualifications (
    StaffID int,
    Qualifications varchar(500),
    PRIMARY KEY(StaffID, Qualifications)
);

CREATE TABLE Teacher (
    StaffID int,
    CoursesTeachingID int,
    PRIMARY KEY(StaffID, CoursesTeachingID)
);

CREATE TABLE TeachingAssistant (
    StaffID int,
    StudentID int,
    CourseID varchar(6),
    PRIMARY KEY(StaffID, StudentID, CourseID)
);

CREATE TABLE Classroom (
    ClassroomID int,
    BuildingName varchar(50),
    PRIMARY KEY(ClassroomID)
);

CREATE TABLE CoursesInClassroom (
    ClassroomID int,
    CourseID varchar(6),
    PRIMARY KEY(ClassroomID, CourseID)
);

CREATE TABLE Department (
    DepartmentID int,
    Name varchar(100),
    HOD_ID int,
    PRIMARY KEY(DepartmentID)
);

CREATE TABLE WorksForDepartment (
    DepartmentID int,
    StaffID int,
    PRIMARY KEY(DepartmentID, StaffID)
);

CREATE TABLE StudiesInDepartment (
    DepartmentID int,
    StudentID int,
    PRIMARY KEY(DepartmentID, StudentID)
);

CREATE TABLE Course (
    CourseID varchar(6),
    Credits int,
    PRIMARY KEY(CourseID)
);

CREATE TABLE CoursePrerequisites (
    CourseID varchar(6),
    Prerequisites varchar(6),
    PRIMARY KEY(CourseID, Prerequisites)
);

CREATE TABLE Dependent (
    StaffID int,
    FirstName varchar(50),
    LastName varchar(50),
    CountryCode int,
    PhoneNumber int,
    EmailID varchar(255),
    Address varchar(500),
    PRIMARY KEY(StaffID, FirstName, LastName)
);

CREATE TABLE Grade (
    Grade real,
    CourseID varchar(6),
    StudentID int,
    PRIMARY KEY(CourseID, StudentID)
);

CREATE TABLE Teaches (
    StudentID int,
    StaffID int,
    PRIMARY KEY(StudentID, StaffID)
);

CREATE TABLE Enrolled (
    StudentID int,
    CourseID varchar(6),
    PRIMARY KEY(StudentID, CourseID)
);

CREATE TABLE Partof (
    TeacherHOD_ID int,
    TeacherMember_ID int,
    DepartmentID int,
    PRIMARY KEY(TeacherHOD_ID, TeacherMember_ID, DepartmentID)
);

CREATE TABLE MentorAStudent (
    StudentID int,
    TeacherID int,
    DepartmentID int,
    PRIMARY KEY(StudentID, TeacherID, DepartmentID)
);

CREATE TABLE Lecture (
    StudentID int,
    TeacherID int,
    CourseID varchar(6),
    ClassroomID int,
    PRIMARY KEY(StudentID, TeacherID, CourseID, ClassroomID)
);

CREATE TABLE InvolvedInACourse (
    StudentID int,
    TeacherID int,
    CourseID varchar(6),
    TeachingAssistantStaffID int,
    PRIMARY KEY(
        StudentID,
        TeacherID,
        CourseID,
        TeachingAssistantStaffID
    )
);

DELIMITER // 
CREATE TRIGGER StudentAgeInsert
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
CREATE TRIGGER StudentAgeUpdate
AFTER
UPDATE
    ON Student FOR EACH ROW BEGIN
UPDATE StudentAge
SET Age = (YEAR(NOW()) - YEAR(NEW.DOB) - (
        DATE_FORMAT(NEW.DOB, '%m%d') < DATE_FORMAT(NOW(), '%m%d')
    )),
    DOB = NEW.DOB
WHERE StudentID = NEW.StudentID;
END //
DELIMITER ;

DELIMITER // 
CREATE TRIGGER StudentAgeDelete
AFTER
DELETE
    ON Student FOR EACH ROW BEGIN
DELETE FROM StudentAge
WHERE StudentID = OLD.StudentID;
END //
DELIMITER ;

DELIMITER // 
CREATE TRIGGER StaffAgeInsert
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
CREATE TRIGGER StaffAgeUpdate
AFTER
UPDATE
    ON Staff FOR EACH ROW BEGIN
UPDATE StaffAge
SET Age = (YEAR(NOW()) - YEAR(NEW.DOB) - (
        DATE_FORMAT(NEW.DOB, '%m%d') < DATE_FORMAT(NOW(), '%m%d')
    )),
    DOB = NEW.DOB
WHERE StaffID = NEW.StaffID;
END //
DELIMITER ;

DELIMITER // 
CREATE TRIGGER StaffAgeDelete
AFTER
DELETE
    ON Staff FOR EACH ROW BEGIN
DELETE FROM StaffAge
WHERE StaffID = OLD.StaffID;
END //
DELIMITER ;

/* Student */
INSERT INTO
    Student
values
    (
        NULL,
        'aaron',
        'monis',
        2,
        'CSE',
        'Dasa',
        123456789123,
        4,
        '2002-01-20',
        '2020-07-19',
        'blue'
    );

INSERT INTO
    Guardian
VALUES
    (
        'Rohan',
        'C',
        '3',
        'New York',
        91,
        7894652315,
        "rohan@gmail.com"
    );

INSERT INTO
    Staff
VALUES
    (
        NULL,
        'Radha',
        'Reddy',
        50000.0,
        1234567891234567,
        123456789123,
        'Hyderabad',
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
        'Mumbai',
        '1970-09-14',
        '1996-12-08',
        'permanent'
    );

UPDATE Student
SET Year = 3
WHERE FirstName = 'aaron';