import Modules
from getpass import getpass
import argparse

def main():
    conn = Modules.db.connect('accounts.db')
    parser = argparse.ArgumentParser()

    parser.add_argument("--register", action="store_true")
    parser.add_argument("--login", action="store_true")

    args = parser.parse_args()
    if args.register:
        print("Register flow")
        username = input("enter username:")
        password = Modules.auth.hash(getpass("enter password:"))
        Modules.db.new_user(conn,username, password)

    if args.login:
        print("Login flow")
        username = input("enter username:")
        hash= Modules.db.find_user_password(conn,username)
        password = getpass("enter password:")
        authentication = Modules.auth.verify(password, hash)
        if authentication:
            print("Access Granted")
        else:
            print("Access Denied")

