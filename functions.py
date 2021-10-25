def student(con, cursor):
    while True:
        print("\nStudent")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student Information")
        print("4. Search Student")
        print("5. View Student")
        print("6. Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            query = "INSERT INTO Student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            student_id = int(input("Enter Student ID: "))
            first_name = input("Enter the Student's First Name: ")
            second_name = input("Enter the Student's Second Name: ")
            year = int(input("Enter the Student's Year: "))
            stream = input("Enter the Student's Stream: ")
            address = input("Enter the Student's Address: ")
            aadhaar = int(input("Enter the Student's Aadhaar Number: "))
            number_of_courses = int(input("Enter the number of courses the student is enrolled in: "))
            dob = input("Enter the Student's Date of Birth (yyyy-mm-dd): ")
            enrollment_date = input("Enter the Student's Enrollment Date (yyyy-mm-dd): ")
            house = input("Enter the Student's House: ")
            cursor.execute(query, (student_id, first_name, second_name, year, stream, address, aadhaar, number_of_courses, dob, enrollment_date, house))
            con.commit()
            number = input("Enter the Student's number (code number): ")
            num_list = number.split(' ')
            if(len(num_list) == 1):
                code = 91
                num = int(num_list[0])
            else:
                code = int(num_list[0])
                num = int(num_list[1])
            query = "INSERT INTO StudentContactNumber VALUES (%s, %s, %s)"
            cursor.execute(query, (student_id, code, num))
            con.commit()
            email_id = input("Enter the Student's EmailID: ")
            query = "INSERT INTO StudentEmailID VALUES (%s, %s)"
            cursor.execute(query, (student_id, email_id))
            con.commit()
            while True:
                print("\nStudent Medical Conditions: ")
                print("1. Add Medical Condition")
                print("2. Back")
                ch = int(input("Enter your choice: "))
                if ch == 1:
                    query = "INSERT INTO Student_MedicalConditions VALUES (%s, %s)"
                    condition = input("Enter the Medical Condition: ")
                    cursor.execute(query, (student_id, condition))
                    con.commit()
                elif ch == 2:
                    break
            while True:
                print("\nStudent Emergency Contacts: ")
                print("1. Add Emergency Contact")
                print("2. Back")
                ch = int(input("Enter your choice: "))
                if ch == 1:
                    query = "INSERT INTO Student_Emergency VALUES (%s, %s, %s)"
                    name = input("Enter the Emergency Contact's Name: ")
                    code = int(input("Enter the Emergency Contact's Telephone Code: "))
                    number = int(input("Enter the Emergency Contact's Telephone Number: "))
                    cursor.execute(query, (student_id, name, code, number))
                    con.commit()
                elif ch == 2:
                    break
            while True:
                print("\nStudent Courses: ")
                print("1. Add Course")
                print("2. Back")
                ch = int(input("Enter your choice: "))
                if ch == 1:
                    query = "INSERT INTO Student_Courses VALUES (%s, %s)"
                    course_id = int(input("Enter the Course ID: "))
                    query1 = "SELECT * FROM Courses WHERE CourseID = %s"
                    cursor.execute(query1, (course_id))
                    result = cursor.fetchone()
                    if result is None:
                        print("Course does not exist")
                        continue
                    cursor.execute(query, (student_id, course_id))
                    con.commit()
                elif ch == 2:
                    break
            while True:
                print("\nStudent Subjects: ")
                print("1. Add Subject")
                print("2. Back")
                ch = int(input("Enter your choice: "))
                if ch == 1:
                    query = "INSERT INTO Guardian VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    student_id = int(input("Enter Student ID: "))
                    first_name = input("Enter the Student's First Name: ")
                    second_name = input("Enter the Student's Second Name: ")
                    address = input("Enter the Student's Address: ")
                    code = int(input("Enter the Emergency Contact's Telephone Code: "))
                    number = int(input("Enter the Emergency Contact's Telephone Number: "))
                    email_id = input("Enter the Student's EmailID: ")
                    cursor.execute(query, (first_name, second_name, student_id, address, code, number, email_id))
                    con.commit()
                elif ch == 2:
                    break
            print("Student added successfully")
        elif choice == 2:
            student_id = int(input("Enter Student ID: "))
            query = "DELETE FROM Student WHERE StudentID = %s"
            cursor.execute(query, (student_id))
            query = "DELETE FROM Guardian WHERE StudentID = %s"
            cursor.execute(query, (student_id))
            query = "DELETE FROM StudentContactNumber WHERE StudentID = %s"
            cursor.execute(query, (student_id))
            query = "DELETE FROM Student_MedicalConditions WHERE StudentID = %s"
            cursor.execute(query, (student_id))
            query = "DELETE FROM Student_Emergency WHERE StudentID = %s"
            cursor.execute(query, (student_id))
            query = "DELETE FROM Student_Courses WHERE StudentID = %s"
            cursor.execute(query, (student_id))
            con.commit()
            print("Student deleted successfully")
        elif choice == 3:
            student_id = int(input("Enter Student ID: "))
            query = "SELECT * FROM Student WHERE StudentID = %s"
            upd_row = dict() 
            cursor.execute(query, (student_id))
            result = cursor.fetchone()
            if result is None:
                print("Student does not exist")
                continue
            print("\nUpdate Student Information")
            print("Press ENTER if no update is required, otherwise enter the new value: ")
            upd_row['FirstName'] = input("1. First Name: ")
            if upd_row['FirstName'] == '':
                upd_row['FirstName'] = result[1]
            upd_row['LastName'] = input("2. Last Name: ")
            if upd_row['LastName'] == '':
                upd_row['LastName'] = result[2]
            upd_row['Year'] = input("3. Year: ")
            if upd_row['Year'] == 0:
                upd_row['Year'] = result[3]
            else:
                upd_row['Year'] = int(upd_row['Year'])
            upd_row['StreamName'] = input("4. Stream: ")
            if upd_row['StreamName'] == '':
                upd_row['StreamName'] = result[4]
            upd_row['Address'] = input("5. Address: ")
            if upd_row['Address'] == '':
                upd_row['Address'] = result[5]
            upd_row['Aadhaar'] = int(input("6. Aadhaar Number: "))
            if upd_row['Aadhaar'] == 0:
                upd_row['Aadhaar'] = result[6]
            else:
                upd_row['Aadhaar'] = int(upd_row['Aadhaar'])
            upd_row['NumberOfCourses'] = int(input("7. Number of Courses: "))
            if upd_row['NumberOfCourses'] == 0:
                upd_row['NumberOfCourses'] = result[7]
            else:
                upd_row['NumberOfCourses'] = int(upd_row['NumberOfCourses'])
            upd_row['DOB'] = input("8. Date of Birth: ")
            if upd_row['DOB'] == '':
                upd_row['DOB'] = result[8]
            upd_row['EnrollmentDate'] = input("9. Enrollment Date: ")
            if upd_row['EnrollmentDate'] == '':
                upd_row['EnrollmentDate'] = result[9]
            upd_row['House'] = input("10. House: ")
            if upd_row['House'] == '':
                upd_row['House'] = result[10]
            query = "UPDATE Student SET StudentID = %s, FirstName = %s, LastName = %s, Year = %s, StreamName = %s, Address = %s, Aadhaar = %s, NumberOfCourses = %s, DOB = %s, EnrollmentDate = %s, House = %s"
            cursor.execute(query, (student_id, upd_row['FirstName'], upd_row['LastName'], upd_row['Year'], upd_row['StreamName'], upd_row['Address'], upd_row['Aadhaar'], upd_row['NumberOfCourses'], upd_row['DOB'], upd_row['EnrollmentDate'], upd_row['House']))
            con.commit()
            print("Student updated successfully")
        elif choice == 4:
            student_id = int(input("Enter Student ID: "))
            query = "SELECT * FROM Student WHERE StudentID = %s"
            cursor.execute(query, (student_id))
            result = cursor.fetchone()
            if result is None:
                print("Student does not exist")
                continue
            print("Student Information: ")
            print("Student ID: ", result[0])
            print("First Name: ", result[1])
            print("Last Name: ", result[2])
            print("Year: ", result[3])
            print("Stream: ", result[4])
            print("Address: ", result[5])
            print("Aadhaar Number: ", result[6])
            print("Number of Courses: ", result[7])
            print("Date of Birth: ", result[8])
            print("Enrollment Date: ", result[9])
            print("House: ", result[10])
        elif choice == 5:
            try:
                query = "SELECT * FROM Student"
                cursor.execute(query)
                result = cursor.fetchall()
                for row in result:
                    print(row)
            except Exception as e:
                print(e)
        elif choice == 6:
            exit()
        else:
            print("Invalid choice")

def staff(con, cursor):
    while True:
        print("\Staff")
        print("1. Add Staff Member")
        print("2. Delete Staff Member")
        print("3. Update Staff Information")
        print("4. Search Staff Member")
        print("5. View Staff Members")
        print("6. Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            query = "INSERT INTO Staff VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            staff_id = int(input("Enter Staff ID: "))
            first_name = input("Enter the Staff Member's First Name: ")
            second_name = input("Enter the Staff Member's Second Name: ")
            salary = float(input("Enter the Staff Member's Salary: "))
            bank_account = int(input("Enter the Staff Member's Bank Account Number: "))
            address = input("Enter the Staff Member's Address: ")
            aadhaar = int(input("Enter the Staff Member's Aadhaar Number: "))
            dob = input("Enter the Student's Date of Birth (yyyy-mm-dd): ")
            Joining_date = input("Enter the Staff Member's Joining Date (yyyy-mm-dd): ")
            permanency = input("Enter the Staff Member's Permanency Status: ")
            cursor.execute(query, (staff_id, first_name, second_name, salary, bank_account, aadhaar, address, dob, Joining_date, permanency))
            con.commit()
            number = input("Enter the Staff Member's number (code number): ")
            num_list = number.split(' ')
            if(len(num_list) == 1):
                code = 91
                num = int(num_list[0])
            else:
                code = int(num_list[0])
                num = int(num_list[1])
            query = "INSERT INTO StaffContactNumber VALUES (%s, %s, %s)"
            cursor.execute(query, (staff_id, code, num))
            con.commit()
            email_id = input("Enter the Staff Member's EmailID: ")
            query = "INSERT INTO StaffEmailID VALUES (%s, %s)"
            cursor.execute(query, (staff_id, email_id))
            con.commit()
            designation = input("Enter the Staff's Designation: ")
            query = "INSERT INTO StaffDesignation VALUES (%s, %s)"
            cursor.execute(query, (staff_id, designation))
            con.commit()
            while True:
                print("\Staff Qualifications: ")
                print("1. Add Qualification")
                print("2. Back")
                ch = int(input("Enter your choice: "))
                if ch == 1:
                    query = "INSERT INTO Staff_Qualifications VALUES (%s, %s)"
                    qualification = input("Enter the Qualification: ")
                    cursor.execute(query, (staff_id, qualification))
                    con.commit()
                elif ch == 2:
                    break
            while True:
                print("\nStaff Medical Conditions: ")
                print("1. Add Condition")
                print("2. Back")
                ch = int(input("Enter your choice: "))
                if ch == 1:
                    query = "INSERT INTO Staff_Medical_Conditions VALUES (%s, %s)"
                    condition = input("Enter the Condition: ")
                    cursor.execute(query, (staff_id, condition))
                    con.commit()
                elif ch == 2:
                    break
            print("Staff Member added successfully")
        elif choice == 2:
            staff_id = int(input("Enter Staff ID: "))
            query = "DELETE FROM Staff WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
            query = "DELETE FROM StaffContactNumber WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
            query = "DELETE FROM StaffEmailID WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
            query = "DELETE FROM StaffDesignation WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
            query = "DELETE FROM Staff_Qualifications WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
            query = "DELETE FROM StaffMedicalConditions WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
            query = "DELETE FROM Teacher WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
            query = "DELETE FROM TeachingAssistant WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
            query = "DELETE FROM WorksForDepartment WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
            query = "DELETE FROM Teaches WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
            query = "DELETE FROM Dependent WHERE StaffID = %s"
            cursor.execute(query, (staff_id))
            con.commit()
        elif choice == 3:
            continue
        elif choice == 4:
            continue
        elif choice == 5:
            try:
                query = "SELECT * FROM Student"
                cursor.execute(query)
                result = cursor.fetchall()
                for row in result:
                    print(row)
            except Exception as e:
                print(e)
        elif choice == 6:
            exit()
        else:
            print("Invalid choice")