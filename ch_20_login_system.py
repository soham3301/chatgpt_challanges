print("=== USER LOGIN ===\n")

username = "Soham"
password = "Python123"
username_list = []
password_list = []

def check_login():
    max_login_attempt = 3
    while 1 <= max_login_attempt:
        username_list.append(str(input("Username: ")))
        password_list.append(str(input("Password: ")))
        max_login_attempt -= 1

        if username in username_list and password in password_list:
            print("\n*** Access Granted ***")
            break
        else:
            username_list.pop()
            password_list.pop()
            print("\nXXX Invalid Credentials. Try Again XXX\n")
    
        if max_login_attempt == 0:
            print("Account Locked")
            break

def main():
    check_login()
main()
