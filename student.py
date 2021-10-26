def student(con, cursor):
    while True:
        print("\nStudent")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student Information")
        print("4. Search Student")
        print("5. View Student")
        print("6. Retrieve the complete data tuples of all students belonging to a particular House.")
        print("7. Retrieve the Names of Students with more than 4 courses")
        print("8. Find the average number of courses of all students who enrolled in a particular year.")
        print("9. Search for students from Mumbai.")
        print("10. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            try:
                query = "INSERT INTO Student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                print(query)
                student_id = int(input("Enter Student ID: "))
                first_name = input("Enter the Student's First Name: ")
                second_name = input("Enter the Student's Second Name: ")
                year = int(input("Enter the Student's Year: "))
                stream = input("Enter the Student's Stream: ")
                address = input("Enter the Student's Address: ")
                aadhaar = int(input("Enter the Student's Aadhaar Number: "))
                number_of_courses = int(
                    input("Enter the number of courses the student is enrolled in: "))
                dob = input("Enter the Student's Date of Birth (yyyy-mm-dd): ")
                enrollment_date = input(
                    "Enter the Student's Enrollment Date (yyyy-mm-dd): ")
                house = input("Enter the Student's House: ")
                cursor.execute(query, (student_id, first_name, second_name, year, stream,
                                       address, aadhaar, number_of_courses, dob, enrollment_date, house))
                num = input("Enter the Student's number: ")
                code = input("Enter the Student's Telephone Code: ")
                if code == '':
                    code = 91
                else:
                    code = int(code)
                query = "INSERT INTO StudentContactNumber VALUES (%s, %s, %s)"
                cursor.execute(query, (student_id, code, num))
                email_id = input("Enter the Student's EmailID: ")
                query = "INSERT INTO StudentEmailID VALUES (%s, %s)"
                cursor.execute(query, (student_id, email_id))
                while True:
                    print("\nStudent Medical Conditions: ")
                    print("1. Add Medical Condition")
                    print("2. Back")
                    ch = int(input("Enter your choice: "))
                    if ch == 1:
                        query = "INSERT INTO Student_MedicalConditions VALUES (%s, %s)"
                        condition = input("Enter the Medical Condition: ")
                        cursor.execute(query, (student_id, condition))
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
                        code = int(
                            input("Enter the Emergency Contact's Telephone Code: "))
                        number = int(
                            input("Enter the Emergency Contact's Telephone Number: "))
                        cursor.execute(query, (student_id, name, code, number))
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
                    elif ch == 2:
                        break
                while True:
                    print("\nStudent Guardians: ")
                    print("1. Add Guardian")
                    print("2. Back")
                    ch = int(input("Enter your choice: "))
                    if ch == 1:
                        query = "INSERT INTO Guardian VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        first_name = input("Enter the Guardian's First Name: ")
                        second_name = input(
                            "Enter the Guardian's Second Name: ")
                        address = input("Enter the Guardian's Address: ")
                        code = input("Enter the Guardian's Telephone Code: ")
                        if code == '':
                            code = 91
                        else:
                            code = int(code)
                        number = int(
                            input("Enter the Guardian's Telephone Number: "))
                        email_id = input("Enter the Guardian's EmailID: ")
                        cursor.execute(
                            query, (first_name, second_name, student_id, address, code, number, email_id))
                    elif ch == 2:
                        break
                con.commit()
                print("Student added successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 2:
            try:
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
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 3:
            try:
                student_id = int(input("Enter Student ID: "))
                query = "SELECT * FROM Student WHERE StudentID = %s"
                upd_row = dict()
                cursor.execute(query, (student_id))
                result = cursor.fetchone()
                if result is None:
                    print("Student does not exist")
                    continue
                print("\nUpdate Student Information")
                print(
                    "Press ENTER if no update is required, otherwise enter the new value: ")
                upd_row['FirstName'] = input("1. First Name: ")
                if upd_row['FirstName'] == '':
                    upd_row['FirstName'] = result['FirstName']
                upd_row['LastName'] = input("2. Last Name: ")
                if upd_row['LastName'] == '':
                    upd_row['LastName'] = result['LastName']
                upd_row['Year'] = input("3. Year: ")
                if upd_row['Year'] == '':
                    upd_row['Year'] = result['Year']
                else:
                    upd_row['Year'] = upd_row['Year']
                upd_row['StreamName'] = input("4. Stream: ")
                if upd_row['StreamName'] == '':
                    upd_row['StreamName'] = result['StreamName']
                upd_row['Address'] = input("5. Address: ")
                if upd_row['Address'] == '':
                    upd_row['Address'] = result['Address']
                upd_row['Aadhaar'] = input("6. Aadhaar Number: ")
                if upd_row['Aadhaar'] == '':
                    upd_row['Aadhaar'] = result['Aadhaar']
                else:
                    upd_row['Aadhaar'] = int(upd_row['Aadhaar'])
                upd_row['NumberOfCourses'] = input("7. Number of Courses: ")
                if upd_row['NumberOfCourses'] == '':
                    upd_row['NumberOfCourses'] = result['NumberOfCourses']
                else:
                    upd_row['NumberOfCourses'] = int(
                        upd_row['NumberOfCourses'])
                upd_row['DOB'] = input("8. Date of Birth: ")
                if upd_row['DOB'] == '':
                    upd_row['DOB'] = result['DOB']
                upd_row['EnrollmentDate'] = input("9. Enrollment Date: ")
                if upd_row['EnrollmentDate'] == '':
                    upd_row['EnrollmentDate'] = result['EnrollmentDate']
                upd_row['House'] = input("10. House: ")
                if upd_row['House'] == '':
                    upd_row['House'] = result['House']
                query = "UPDATE Student SET StudentID = %s, FirstName = %s, LastName = %s, Year = %s, StreamName = %s, Address = %s, Aadhaar = %s, NumberOfCourses = %s, DOB = %s, EnrollmentDate = %s, House = %s"
                cursor.execute(query, (student_id, upd_row['FirstName'], upd_row['LastName'], upd_row['Year'], upd_row['StreamName'],
                                       upd_row['Address'], upd_row['Aadhaar'], upd_row['NumberOfCourses'], upd_row['DOB'], upd_row['EnrollmentDate'], upd_row['House']))
                con.commit()
                print("Student updated successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 4:
            student_id = int(input("Enter Student ID: "))
            query = "SELECT * FROM Student WHERE StudentID = %s"
            cursor.execute(query, (student_id))
            result = cursor.fetchone()
            if result is None:
                print("Student does not exist")
                continue
            print("Student Information: ")
            print("Student ID: ", result['StudentID'])
            print("First Name: ", result['FirstName'])
            print("Last Name: ", result['LastName'])
            print("Year: ", result['Year'])
            print("Stream: ", result['StreamName'])
            print("Address: ", result['Address'])
            print("Aadhaar Number: ", result['Aadhaar'])
            print("Number of Courses: ", result['NumberOfCourses'])
            print("Date of Birth: ", result['DOB'])
            print("Enrollment Date: ", result['EnrollmentDate'])
            print("House: ", result['House'])
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
            query = "SELECT * FROM Student WHERE HOUSE = %s"
            house = input(
                "Enter the House whose Students data you wish to view: ")
            cursor.execute(query, (house))
            result = cursor.fetchall()
            if result is None:
                print("No Students in this House")
                continue
            for row in result:
                print(row)
        elif choice == 7:
            query = "SELECT FirstName, LastName FROM Student WHERE NumberOfCourses > 4"
            cursor.execute(query)
            result = cursor.fetchall()
            if result is None:
                print("No Students with more than 4 courses")
                continue
            for row in result:
                print(row['FirstName'], row['LastName'])
        elif choice == 8:
            query = "SELECT AVG(NumberOfCourses) AS Average FROM Student WHERE YEAR(EnrollmentDate) = %s"
            year = int(input("Enter the Enrollment year: "))
            cursor.execute(query, (year))
            result = cursor.fetchone()
            print("Average number of courses for the enrollment year: ",
                  result['Average'])
        elif choice == 9:
            query = "SELECT FirstName, LastName FROM Student WHERE Address LIKE '%Mumbai%'"
            cursor.execute(query)
            result = cursor.fetchall()
            if result is None:
                print("No Students in Mumbai")
                continue
            for row in result:
                print(row['FirstName'], row['LastName'])
        elif choice == 10:
            return
        else:
            print("Invalid choice")


def guardian(con, cursor):
    while True:
        print("1. Add Guardian")
        print("2. Delete Guardian")
        print("3. Update Guardian")
        print("4. View Guardians of a Student")
        print("5. View Guardian Information")
        print("6. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            try:
                query = "INSERT INTO Guardian VALUES (%s, %s, %s, %s, %s, %s, %s)"
                student_id = int(input("Enter Student ID: "))
                first_name = input("Enter the Guardian's First Name: ")
                second_name = input("Enter the Guardian's Second Name: ")
                address = input("Enter the Guardian's Address: ")
                code = input("Enter the Guardian's Telephone Code: ")
                if code == '':
                    code = 91
                else:
                    code = int(code)
                number = int(input("Enter the Guardian's Telephone Number: "))
                email_id = input("Enter the Guardian's EmailID: ")
                cursor.execute(query, (first_name, second_name,
                                       student_id, address, code, number, email_id))
                con.commit()
                print("Guardian added successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 2:
            try:
                student_id = int(input("Enter Student ID: "))
                first_name = input("Enter the Guardian's First Name: ")
                last_name = input("Enter the Guardian's Last Name: ")
                query = "DELETE FROM Guardian WHERE FirstName = %s AND LastName = %s AND StudentID = %s"
                cursor.execute(query, (first_name, last_name, student_id))
                con.commit()
                print("Guardian deleted successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 3:
            try:
                student_id = int(input("Enter Student ID: "))
                first_name = input("Enter the Guardian's First Name: ")
                last_name = input("Enter the Guardian's Last Name: ")
                upd_row = dict()
                query = "SELECT * FROM Guardian WHERE FirstName = %s AND LastName = %s AND StudentID = %s"
                cursor.execute(query, (first_name, last_name, student_id))
                result = cursor.fetchone()
                if result == None:
                    print("Guardian does not exist")
                    continue
                print("Guardian Information: ")
                print(
                    "Press ENTER if no update is required, otherwise enter the new value: ")
                upd_row['FirstName'] = input("First Name: ")
                if upd_row['FirstName'] == '':
                    upd_row['FirstName'] = result['FirstName']
                upd_row['LastName'] = input("Last Name: ")
                if upd_row['LastName'] == '':
                    upd_row['LastName'] = result['LastName']
                upd_row['Address'] = input("Address: ")
                if upd_row['Address'] == '':
                    upd_row['Address'] = result['Address']
                upd_row['CountryCode'] = input("Country Code")
                if upd_row['CountryCode'] == '':
                    upd_row['CountryCode'] = result['CountryCode']
                else:
                    upd_row['CountryCode'] = int(upd_row['CountryCode'])
                upd_row['PhoneNumber'] = input("Phone Number: ")
                if upd_row['PhoneNumber'] == '':
                    upd_row['PhoneNumber'] = result['PhoneNumber']
                else:
                    upd_row['PhoneNumber'] = int(upd_row['PhoneNumber'])
                upd_row['EmailID'] = input("Email ID: ")
                if upd_row['EmailID'] == '':
                    upd_row['EmailID'] = result['EmailID']
                query = "UPDATE Guardian SET FirstName = %s, LastName = %s, Address = %s, CountryCode = %s, PhoneNumber = %s, EmailID = %s WHERE FirstName = %s AND LastName = %s AND StudentID = %s"
                cursor.execute(query, (upd_row['FirstName'], upd_row['LastName'], upd_row['Address'],
                                       upd_row['CountryCode'], upd_row['PhoneNumber'], upd_row['EmailID'], first_name, last_name, student_id))
                con.commit()
                print("Guardian updated successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 4:
            student_id = int(input("Enter Student ID: "))
            query = "SELECT * FROM Guardian WHERE StudentID = %s"
            cursor.execute(query, (student_id))
            result = cursor.fetchall()
            if result == None:
                print("Guardian does not exist")
                continue
            print("Guardian Information: ")
            for row in result:
                print(row)
        elif choice == 5:
            first_name = input("Enter the Guardian's First Name: ")
            last_name = input("Enter the Guardian's Last Name: ")
            query = "SELECT * FROM Guardian WHERE FirstName = %s AND LastName = %s"
            cursor.execute(query, (first_name, last_name))
            result = cursor.fetchone()
            if result == None:
                print("Guardian does not exist")
                continue
            print("Guardian Information: ")
            print("Student ID: ", result['StudentID'])
            print("First Name: ", result['FirstName'])
            print("Last Name: ", result['LastName'])
            print("Address: ", result['Address'])
            print("Country Code: ", result['CountryCode'])
            print("Phone Number: ", result['PhoneNumber'])
            print("Email ID: ", result['EmailID'])
        elif choice == 6:
            return
        else:
            print("Invalid choice")

def student_contact(con, cursor):
    while True:
        print("1. Add Student Contact Number")
        print("2. Delete Student Contact Number")
        print("3. Update Student Contact Number")
        print("4. View Student Contact Numbers of a Student")
        print("5. Find Student Contact Number Information")
        print("6. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            try:
                query = "INSERT INTO StudentContactNumber VALUES (%s, %s, %s)"
                student_id = int(input("Enter Student ID: "))
                code = input("Enter the Student's Telephone Code: ")
                if code == '':
                    code = 91
                else:
                    code = int(code)
                number = int(input("Enter the Student's Telephone Number: "))
                cursor.execute(query, (student_id, code, number))
                con.commit()
                print("Student Contact Number added successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 2:
            try:
                student_id = int(input("Enter Student ID: "))
                num = int(input("Enter the Student's Number: "))
                query = "DELETE FROM StudentContactNumber WHERE PhoneNumber = %s AND StudentID = %s"
                cursor.execute(query, (num, student_id))
                con.commit()
                print("Student Contact Number deleted successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 3:
            try:
                student_id = int(input("Enter Student ID: "))
                num = int(input("Enter the Student's Number: "))
                upd_row = dict()
                query = "SELECT * FROM StudentContactNumber WHERE PhoneNumber AND StudentID = %s"
                cursor.execute(query, (num, student_id))
                result = cursor.fetchone()
                if result == None:
                    print("Contact does not exist")
                    continue
                print("Contact Information: ")
                print(
                    "Press ENTER if no update is required, otherwise enter the new value: ")
                upd_row['PhoneNumber'] = input("Phone Number: ")
                if upd_row['PhoneNumber'] == '':
                    upd_row['PhoneNumber'] = result['PhoneNumber']
                else:
                    upd_row['PhoneNumber'] = int(upd_row['PhoneNumber'])
                upd_row['CountryCode'] = input("Country Code: ")
                if upd_row['CountryCode'] == '':
                    upd_row['CountryCode'] = result['CountryCode']
                else:
                    upd_row['CountryCode'] = int(upd_row['CountryCode'])
                query = "UPDATE StudentContactNumber SET PhoneNumber = %s, CountryCode = %s WHERE PhoneNumber = %s AND StudentID = %s"
                cursor.execute(query, (upd_row['PhoneNumber'], upd_row['CountryCode'], num, student_id))
                con.commit()
                print("Contact updated successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 4:
            student_id = int(input("Enter Student ID: "))
            query = "SELECT * FROM StudentContactNumber WHERE StudentID = %s"
            cursor.execute(query, (student_id))
            result = cursor.fetchall()
            if result == None:
                print("Contact does not exist")
                continue
            print("Contact Information: ")
            for row in result:
                print(row)
        elif choice == 5:
            student_id = int(input("Enter Student ID: "))
            num = int(input("Enter the Student's Number: "))
            query = "SELECT * FROM StudentContactNumber WHERE PhoneNumber = %s AND StudentID = %s"
            cursor.execute(query, (num, student_id))
            result = cursor.fetchone()
            if result == None:
                print("Contact does not exist")
                continue
            else:
                print("Found!")
                continue
        elif choice == 6:
            return
        else:
            print("Invalid choice")

def student_email(con, cursor):
    while True:
        print("1. Add Student Email")
        print("2. Delete Student Email")
        print("3. Update Student Email")
        print("4. View Email IDs of a Student")
        print("5. Find Student Email ID Information")
        print("6. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            try:
                query = "INSERT INTO StudentEmailID VALUES (%s, %s)"
                student_id = int(input("Enter Student ID: "))
                email = input("Enter the Student's Email ID: ")
                cursor.execute(query, (student_id, email))
                con.commit()
                print("Student Email added successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 2:
            try:
                student_id = int(input("Enter Student ID: "))
                email = input("Enter the Student's Email ID: ")
                query = "DELETE FROM StudentEmailID WHERE EmailID = %s AND StudentID = %s"
                cursor.execute(query, (email, student_id))
                con.commit()
                print("Student Email deleted successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 3:
            try:
                student_id = int(input("Enter Student ID: "))
                email = input("Enter the Student's Email ID: ")
                upd_row = dict()
                query = "SELECT * FROM StudentEmailID WHERE EmailID = %s AND StudentID = %s"
                cursor.execute(query, (email, student_id))
                result = cursor.fetchone()
                if result == None:
                    print("Email does not exist")
                    continue
                print("Email Information: ")
                print(
                    "Press ENTER if no update is required, otherwise enter the new value: ")
                upd_row['EmailID'] = input("Email ID: ")
                if upd_row['EmailID'] == '':
                    upd_row['EmailID'] = result['EmailID']
                query = "UPDATE StudentEmailID SET EmailID = %s WHERE EmailID = %s AND StudentID = %s"
                cursor.execute(query, (upd_row['EmailID'], email, student_id))
                con.commit()
                print("Email updated successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 4:
            student_id = int(input("Enter Student ID: "))
            query = "SELECT * FROM StudentEmailID WHERE StudentID = %s"
            cursor.execute(query, (student_id))
            result = cursor.fetchall()
            if result == None:
                print("Email does not exist")
                continue
            print("Email Information: ")
            for row in result:
                print(row)
        elif choice == 5:
            student_id = int(input("Enter Student ID: "))
            email = input("Enter the Student's Email ID: ")
            query = "SELECT * FROM StudentEmailID WHERE EmailID = %s AND StudentID = %s"
            cursor.execute(query, (email, student_id))
            result = cursor.fetchone()
            if result == None:
                print("Email does not exist")
                continue
            else:
                print("Found!")
                continue
        elif choice == 6:
            return
        else:
            print("Invalid choice")

def student_medical_conditions(con, cursor):
    while True:
        print("1. Add Student Medical Conditions")
        print("2. Delete Student Medical Conditions")
        print("3. Update Student Medical Conditions")
        print("4. View Medical Conditions of a Student")
        print("5. View all Medical Condition Information")
        print("6. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            try:
                query = "INSERT INTO Student_MedicalConditions VALUES (%s, %s)"
                student_id = int(input("Enter Student ID: "))
                medi = input("Enter the Student's Medical Conditions: ")
                cursor.execute(query, (student_id, medi))
                con.commit()
                print("Student's Medical Conditions added successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 2:
            try:
                student_id = int(input("Enter Student ID: "))
                medi = input("Enter the Student's Medical Conditions: ")
                query = "DELETE FROM Student_MedicalConditions WHERE MedicalConditions = %s AND StudentID = %s"
                cursor.execute(query, (medi, student_id))
                con.commit()
                print("Student's Medical Conditions deleted successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 3:
            try:
                student_id = int(input("Enter Student ID: "))
                medi = input("Enter the Student's Medical Conditions: ")
                upd_row = dict()
                query = "SELECT * FROM Student_MedicalConditions WHERE MedicalConditions = %s AND StudentID = %s"
                cursor.execute(query, (medi, student_id))
                result = cursor.fetchone()
                if result == None:
                    print("Medical Condition does not exist")
                    continue
                print("Medical Condition Information: ")
                print(
                    "Press ENTER if no update is required, otherwise enter the new value: ")
                upd_row['MedicalConditions'] = input("Medical Conditions: ")
                if upd_row['MedicalConditions'] == '':
                    upd_row['MedicalConditions'] = result['MedicalConditions']
                query = "UPDATE Student_MedicalConditions SET MedicalConditions = %s WHERE MedicalConditions = %s AND StudentID = %s"
                cursor.execute(query, (upd_row['MedicalConditions'], medi, student_id))
                con.commit()
                print("Medical Conditions updated successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 4:
            student_id = int(input("Enter Student ID: "))
            query = "SELECT * FROM Student_MedicalConditions WHERE StudentID = %s"
            cursor.execute(query, (student_id))
            result = cursor.fetchall()
            if result == None:
                print("Medical Condition does not exist")
                continue
            print("Medical Condition Information: ")
            for row in result:
                print("Medical Condition:", row['MedicalConditions'])
        elif choice == 5:
            student_id = int(input("Enter Student ID: "))
            email = input("Enter the Student's Email ID: ")
            query = "SELECT * FROM Student_MedicalConditions;"
            cursor.execute(query)
            result = cursor.fetchall()
            if result == None:
                print("Email does not exist")
                continue
            else:
                for row in result:
                    print("Student ID:", row['StudentID'])
                    print("Medical Condition:", row['MedicalConditions'])
        elif choice == 6:
            return
        else:
            print("Invalid choice")

def student_medical_conditions(con, cursor):
    while True:
        print("1. Add Student Courses")
        print("2. Delete Student Courses")
        print("3. Update Student Courses")
        print("4. View Courses of a Student")
        print("6. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            try:
                query = "INSERT INTO Student_MedicalConditions VALUES (%s, %s)"
                student_id = int(input("Enter Student ID: "))
                medi = input("Enter the Student's Medical Conditions: ")
                cursor.execute(query, (student_id, medi))
                con.commit()
                print("Student's Medical Conditions added successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 2:
            try:
                student_id = int(input("Enter Student ID: "))
                medi = input("Enter the Student's Medical Conditions: ")
                query = "DELETE FROM Student_MedicalConditions WHERE MedicalConditions = %s AND StudentID = %s"
                cursor.execute(query, (medi, student_id))
                con.commit()
                print("Student's Medical Conditions deleted successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 3:
            try:
                student_id = int(input("Enter Student ID: "))
                medi = input("Enter the Student's Medical Conditions: ")
                upd_row = dict()
                query = "SELECT * FROM Student_MedicalConditions WHERE MedicalConditions = %s AND StudentID = %s"
                cursor.execute(query, (medi, student_id))
                result = cursor.fetchone()
                if result == None:
                    print("Medical Condition does not exist")
                    continue
                print("Medical Condition Information: ")
                print(
                    "Press ENTER if no update is required, otherwise enter the new value: ")
                upd_row['MedicalConditions'] = input("Medical Conditions: ")
                if upd_row['MedicalConditions'] == '':
                    upd_row['MedicalConditions'] = result['MedicalConditions']
                query = "UPDATE Student_MedicalConditions SET MedicalConditions = %s WHERE MedicalConditions = %s AND StudentID = %s"
                cursor.execute(query, (upd_row['MedicalConditions'], medi, student_id))
                con.commit()
                print("Medical Conditions updated successfully")
            except Exception as e:
                con.rollback()
                print(e)
                continue
        elif choice == 4:
            student_id = int(input("Enter Student ID: "))
            query = "SELECT * FROM Student_MedicalConditions WHERE StudentID = %s"
            cursor.execute(query, (student_id))
            result = cursor.fetchall()
            if result == None:
                print("Medical Condition does not exist")
                continue
            print("Medical Condition Information: ")
            for row in result:
                print("Medical Condition:", row['MedicalConditions'])
        elif choice == 5:
            student_id = int(input("Enter Student ID: "))
            email = input("Enter the Student's Email ID: ")
            query = "SELECT * FROM Student_MedicalConditions;"
            cursor.execute(query)
            result = cursor.fetchall()
            if result == None:
                print("Email does not exist")
                continue
            else:
                for row in result:
                    print("Student ID:", row['StudentID'])
                    print("Medical Condition:", row['MedicalConditions'])
        elif choice == 6:
            return
        else:
            print("Invalid choice")