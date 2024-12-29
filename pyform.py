import sys
import re

def parse_login_file(login_file):
    with open(login_file, 'r') as file:
        login_req = file.readlines()

    num_lines = 0
    black = 0

    for line in login_req:
        num_lines += 1

    for line in login_req:
        if black == (num_lines - 1):
            body = line.strip()
            break

        line = line.strip() # strip off the \n
        line = re.split(r'[ ]',line) #
        print(line)
        black += 1

    print (body)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 <.py> <login.req>")
        sys.exit(1)

login_file = sys.argv[1]
parse_login_file(login_file)
