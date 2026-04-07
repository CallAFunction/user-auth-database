import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--register", action="store_true")
parser.add_argument("--login", action="store_true")

args = parser.parse_args()

if args.register:
    print("Register flow")

if args.login:
    print("Login flow")