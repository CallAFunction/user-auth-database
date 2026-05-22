import Modules
from getpass import getpass
import argparse

def main():
    conn = Modules.db.connect('accounts.db')
    parser = argparse.ArgumentParser()

    parser.add_argument("--register", action="store_true")
    parser.add_argument("--login", action="store_true")

    args = parser.parse_args()
    #register argument
    if args.register:
        print("Register flow")
        username = input("enter username:")
        password = Modules.auth.hash(getpass("enter password:"))
        Modules.db.new_user(conn,username, password)
    #login argument
    elif args.login:
        print("Login flow")
        username = input("enter username:")
        hash= Modules.db.find_user_password(conn,username)
        if hash is None:
            print("user not found. please use the --register argument to add a user.")
            exit
        else:
            password = getpass("enter password:")
            authentication = Modules.auth.verify(password, hash)
            if authentication:
                print("Access Granted")
            else:
                print("Access Denied")
    else:
        print("unrecognised argument. Please use --register to create a user with a password, or --login to authenticate.")

