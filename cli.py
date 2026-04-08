from getpass import getpass
import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--register", action="store_true")
    parser.add_argument("--login", action="store_true")

    args = parser.parse_args()
    if args.register:
        print("Register flow")
        username = input("enter username:")
        password = hash(getpass("enter password:"))
        new_user(username, password)

    if args.login:
        print("Login flow")

