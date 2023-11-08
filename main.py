logged_in_user = None
lis = {}

from cryptography.fernet import Fernet
from maskpass import askpass
import os

anonymous_menu = {"1": "Sign In", "2": "Sign Up", "3": "Forgot Password?", "4": "Exit"}
user_menu = {"1": "Change Recovery Options", "2": "Add/Change Email", "3": "Sign Out", "4": "Exit"}
admin_menu = {"1": "Add a User", "2": "Delete a User", "3": "Change a User's Password", "4": "Logout", "5": "Exit"}
d={"uppercase letter": (65, 90), "lowercase letter": (97, 122), "number": (40, 57), "special character": (0, 1114111)}
user_designations = {"Admin", "Staff", "User"}

def get_password(mode:int=0) -> str:
    if mode == 1:
        return askpass()
    return input("Enter your password: ")

def set_up_recovery(username):
    q = input("Enter a question:")
    a = input("Enter an answer:")
    lis[username]["recovery"]["question"] = q
    lis[username]["recovery"]["answer"] = a
    
def analyser(username:str, password:str) -> dict:
    details = dict.fromkeys(d.keys(), 0)
    for i in password:
        for j in d:
            if ord(i) >= d[j][0] and ord(i) <= d[j][1]:
                details[j] = details[j]+1
                break
    return {"username": username, "password": password, "details": details, "length": len(password)}

def check_(result:dict) -> tuple:
    state, message= False, str()
    if result["length"] < 8:
        message+="Password must contain atleast 8 characters.\n"
    not_okay=[]
    for i in result["details"]:
        if result["details"][i] == 0:
            not_okay.append(i)
    if not_okay != []:
        message+=f"Password must contain atleast one {", one ".join(not_okay)}."
    if message=="":
        state = True
    return (state, message)

def main(logged_in_user:str, chi:str=None):
    while True:
        print("\n##MENU##")
        if logged_in_user:
            if lis[logged_in_user]["designation"] == "Admin":
                x=""
                for i in admin_menu:
                    x+=(f"[{i}] {admin_menu[i]}\n")
                print(x[:-1])
                if not chi:
                    ch = input("Enter your choice:")
                else:
                    ch = chi
                if ch in admin_menu:
                    if ch == "1":
                        username=input("Enter username: ")
                        if username in lis:
                            print("User already Exists!")
                        else:
                            password = get_password()
                            key = Fernet.generate_key()
                            f = Fernet(key)
                            token = f.encrypt(bytes(password, encoding='utf-8'))
                            lis[username] = {"key": key, "token": token, "email": "", "designation": "User", "recovery": dict(question="", answer="")}
                            print("User added successfully!")
                    elif ch == "2":
                        username=input("Enter username: ")
                        if username in lis:
                            lis.pop(username)
                        else:
                            print("User doesn't Exist!")
                    elif ch == "3":
                        username=input("Enter username: ")
                        if username in lis:
                            password = get_password()
                            f = Fernet(lis[username]["key"])
                            token = f.encrypt(bytes(password, encoding='utf-8'))
                            lis[username]["token"] = token
                        else:
                            print("User doesn't Exist!")
                    elif ch == "4":
                        logged_in_user = None
                        with open(os.path.join(os.getcwd(), "main.py"), 'r') as f:
                            l = f.readlines()
                        l[0] = 'logged_in_user = None\n'
                        with open(os.path.join(os.getcwd(), "main.py"), 'w') as f:
                            f.writelines(l)
                    else:
                        break
            elif lis[logged_in_user]["designation"] == "User":
                x=""
                for i in user_menu:
                    x+=(f"[{i}] {user_menu[i]}\n")
                print(x[:-1])
                if not chi:
                    ch = input("Enter your choice:")
                else:
                    ch = chi
                if ch in user_menu:
                    if ch == "1":
                        set_up_recovery(logged_in_user)
                    elif ch == "2":
                        if lis[logged_in_user]["email"] == "":
                            lis[logged_in_user]["email"] = input("Add an Email: ")
                        else:
                            lis[logged_in_user]["email"] = input("Change your Email from {} to: ".format(lis[logged_in_user]["email"]))
                    elif ch == "3":
                        logged_in_user = None
                        with open(os.path.join(os.getcwd(), "main.py"), 'r') as f:
                            l = f.readlines()
                        l[0] = 'logged_in_user = None\n'
                        with open(os.path.join(os.getcwd(), "main.py"), 'w') as f:
                            f.writelines(l)
                    elif ch == "4":
                        break
            else:
                pass
        else:
            x=""
            for i in anonymous_menu:
                x+=(f"[{i}] {anonymous_menu[i]}\n")
            print(x[:-1])
            if not chi:
                ch = input("Enter your choice:")
            else:
                ch = chi
            if ch in anonymous_menu:
                if ch == "1":
                    username=input("Enter your username: ")
                    password = get_password()
                    if username in lis:
                        f = Fernet(lis[username]["key"])
                        if f.decrypt(lis[username]["token"]).decode() == password:
                            logged_in_user = username
                            print("Signin successful!")
                            with open(os.path.join(os.getcwd(), "main.py"), 'r') as f:
                                l = f.readlines()
                            l[0]='logged_in_user = "{}"\n'.format(username)
                            l[1]="""lis = """+"""{}\n""".format(lis)
                            with open(os.path.join(os.getcwd(), "main.py"), 'w') as f:
                                f.writelines(l)
                            continue
                    print("Login credentials invalid!")
                elif ch == "2":
                    username=input("Enter your username: ")
                    if username in lis:
                        print("A user already exists with the username {}.".format(username))
                        continue
                    password = get_password()
                    final_result = check_(analyser(username, password))
                    if final_result[0]:
                        key = Fernet.generate_key()
                        f = Fernet(key)
                        token = f.encrypt(bytes(password, encoding='utf-8'))
                        lis[username] = {"key": key, "token": token, "email": "", "designation": "User", "recovery": dict(question="", answer="")}
                        cho = input("Would you like to add recovery to your account [Y/N]:").upper()
                        if cho == "Y":
                            set_up_recovery(username)
                        continue
                    print(final_result[1])
                elif ch == "3":
                    username=input("Enter your username: ")
                    if not lis[username]["recovery"]["question"] == "":
                        print("Answer the following question to recover your account:")
                        ans = input(lis[username]["recovery"]["question"])
                        if ans == lis[username]["recovery"]["answer"]:
                            password = get_password()
                            final_result = check_(analyser(username, password))
                            if final_result[0]:
                                f = Fernet(lis[username]["key"])
                                token = f.encrypt(bytes(password, encoding='utf-8'))
                                lis[username]["token"] = token
                elif ch == "4":
                    break
            else:
                print(f"Please enter valid input[1-{len(anonymous_menu)}].")
        

if __name__=="__main__":
    main(logged_in_user=logged_in_user)
