import json, os, time

database = {}
allgood = False

if os.path.exists("database.json"):
    with open("database.json", "r") as f:
        database = json.load(f)
else:
    with open("database.json", "w") as f:
        json.dump(database, f)

try:
    while True:
        os.system("clear")

        choice = input("0: login\n1: register\n\n")
        if choice == "0":

            # login
            os.system("clear")
            username = input("username: ")

            if not username in database:
                print("username not found")
                time.sleep(1.5)
            else:
                for i in range(3):
                    password = input("password: ")
                    if password == database[username]:
                        allgood = True
                        break
                    elif i < 2:
                        print("incorrect password, try again")
                if allgood:
                    break
        elif choice == "1":

            # register
            os.system("clear")
            while True:
                username = input("username: ")
                if not username in database:
                    password = input("password: ")
                    
                    database[username] = password
                    with open("database.json", "w") as f:
                        json.dump(database, f)
                    allgood = True
                    break
                else:
                    print("username already in use")
            if allgood:
                break
        else:
            print("Please type 0 or 1")
            time.sleep(2)
except KeyboardInterrupt:
    print("losing")