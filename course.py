def course(con, cursor):
    while True:
        print("\Courses And Classrooms")
        print("1. Insert course")
        print("2. Delete course")
        print("3. Insert a course prerequisite")
        print("4. Delete a course prerequisite")
        print("5. Insert a classroom")
        print("6. Delete a classroom")
        print("7. Insert a Course-Classroom pair")
        print("8. Delete a Course-Classroom pair")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            try:
                course_id = input("Enter Course ID: ").strip()
                credits = input("Enter the credits")
                try:
                    credits = int(credits)
                except:
                    print("Error: enter a number!")
                    continue

                query = "INSERT INTO Course VALUES (%s %s)"
                cursor.execute(query, (course_id, credits))

                con.commit()
                print("Course added!")

            except Exception as e:
                con.rollback()
                print(e)
                continue

        elif choice == 2:
            try:
                course_id = input("Enter Course ID: ").strip()
                query = "DELETE FROM Course WHERE (CourseID = %s)"
                cursor.execute(query, (course_id))

                con.commit()
                print("Course deleted!")

            except Exception as e:
                con.rollback()
                print(e)
                continue

        elif choice == 3:
            try:
                course_id = input("Enter Course ID: ").strip()
                prereq = input(
                    "Enter Course ID of Prerequisite Course: ").strip()

                query = "INSERT INTO CoursePrerequisites VALUES (%s, %s)"
                cursor.execute(query, (course_id, prereq))

                con.commit()
                print("Course prerequisite added!")

            except Exception as e:
                con.rollback()
                print(e)
                continue

        elif choice == 4:
            try:
                course_id = input("Enter Course ID: ").strip()
                prereq = input(
                    "Enter Course ID of Prerequisite Course: ").strip()

                query = "DELETE FROM CoursePrerequisites WHERE (CourseID = %s, Prerequisites = %s)"
                cursor.execute(query, (course_id, prereq))

                con.commit()
                print("Course prerequisite deleted!")

            except Exception as e:
                con.rollback()
                print(e)
                continue

        elif choice == 5:
            try:
                classroom_id = input("Enter Classroom ID: ").strip()
                BuildingName = input(
                    "Enter the Name of the Building: ").strip()

                query = "INSERT INTO Classroom VALUES (%s, %s)"
                cursor.execute(query, (classroom_id, BuildingName))

                con.commit()
                print("Classroom added!")

            except Exception as e:
                con.rollback()
                print(e)
                continue

        elif choice == 6:
            try:
                classroom_id = input("Enter Classroom ID: ").strip()

                query = "DELETE FROM Classroom WHERE (ClassroomID = %s)"
                cursor.execute(query, (classroom_id))

                con.commit()
                print("Classroom deleted!")

            except Exception as e:
                con.rollback()
                print(e)
                continue

        elif choice == 7:
            try:
                classroom_id = input("Enter Classroom ID: ").strip()
                course_id = input(
                    "Enter the Course ID: ").strip()

                query = "INSERT INTO CoursesInClassroom VALUES (%s, %s)"
                cursor.execute(query, (classroom_id, course_id))

                con.commit()
                print("Course-Classroom pair added!")

            except Exception as e:
                con.rollback()
                print(e)
                continue

        elif choice == 8:
            try:
                classroom_id = input("Enter Classroom ID: ").strip()
                course_id = input(
                    "Enter the Course ID: ").strip()

                query = "DELETE FROM CoursesInClassroom WHERE (ClassroomID = %s, CourseID = %s)"
                cursor.execute(query, (classroom_id, course_id))

                con.commit()
                print("Course-Classroom pair added!")

            except Exception as e:
                con.rollback()
                print(e)
                continue
