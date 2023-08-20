import time
users = {}
status = ""

def displayMenu():
    global status
    status = input("Do you have a login account? y/n? Or press q to quit.\n")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
    elif status == "q":
        quit()

def newUser():
    createlogin = input("Create a login name: ")
    if createlogin in users:
        print("\nLogin name already exists")
    else:
        createPassw = input("Create password: ")
        users[createlogin] = createPassw
        print("\n User created!\n ")
        logins=open("/Users/bbarafwa/Desktop/python/login.txt", "a")
        logins.write("\n"+ createlogin + " " + createPassw)
        logins.close()

def oldUser():
    login = input("Enter login name: ")
    passw = input("Enter password: ")

    #check if user exists and login matches password

    if login in users and users[login] == passw:
        print("\nLogin successful!\n")
        print("User:", login, "accessed the system on:", time.asctime())
    else:
        print("\nUser doesn't exist or wrong password!\n")

while status != "q":
    status = displayMenu()




