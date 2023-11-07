logged_in_user = None
lis = {}

from cryptography.fernet import Fernet
from maskpass import askpass

anonymous_menu = {"1": "Sign In", "2": "Sign Up", "3": "Forgot Password?", "4": "Exit"}
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

def main(ch=None):
    while True:
        x=""
        print("##MENU##")
        if not logged_in_user:
            for i in anonymous_menu:
                x+=(f"[{i}] {anonymous_menu[i]}\n")
            print(x[:-1])
            if not ch:
                ch = input("Enter your choice:")
            if ch in anonymous_menu:
                if ch == "1":
                    username=input("Enter your username: ")
                    password = get_password()
                    if username in lis:
                        f = Fernet(lis[username]["key"])
                        if f.decrypt(lis[username]["token"]).decode() == password:
                            logged_in_user = username
                            print("Signin successful!")
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
                        lis[username] = {"key": key, "token": token, "designation": "User", "recovery": dict(question="", answer="")}
                        ch = input("Would you like to add recovery to your account [Y/N]:").upper()
                        if ch == "Y":
                            set_up_recovery(username)
                        continue
                    print(final_result[1])
                elif ch == "3":
                    username=input("Enter your username: ")
                    if not lis[username]["recovery"]["question"] == "":
                        print("Answer the following question to recover your account:")
                        ans = input(lis[username]["recovery"]["question"])
                        if ans == lis[username]["recovery"]["answer"]:
                            pass
                    print(username)
                elif ch == "4":
                    break
            else:
                print(f"Please enter valid input[1-{len(anonymous_menu)}].")
        

if __name__=="__main__":
    main()