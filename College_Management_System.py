import subprocess as sp
import pymysql
import pymysql.cursors

if __name__ == "__main__":
    while(1):
        tmp = sp.call('clear', shell=True)
        username = input("Username: ")
        password = input("Password: ")
        try:
            con = pymysql.connect(host='localhost',
                                  port=3306,
                                  user=username,
                                  password=password,
                                  db='COLLEGE_MANAGEMENT_SYSTEM',
                                  cursorclass=pymysql.cursors.DictCursor)
            tmp = sp.call('clear', shell=True)
            if(con.open):
                print("Connected")
            else:
                print("Failed to connect")
            tmp = input("Enter any key to CONTINUE>")
            with con.cursor() as cur:
                while(1):
                    tmp = sp.call('clear', shell=True)
                    print("Login/Register:")
                    print("1. Login as Administrator")
                    print("2. Login as User")
                    print("3. Register as User")
                    print("4. Exit")
                    choice = int(input(""))
                    if choice == 1:
                        exit()
                    elif choice == 2:
                        exit()
                    elif choice == 3:
                        exit()
                    elif choice == 4:
                        exit()
                    else:
                        print("Invalid Choice.")

        except Exception as e:
            tmp = sp.call('clear', shell=True)
            print(e)
            print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
            tmp = input("Enter any key to CONTINUE>")
