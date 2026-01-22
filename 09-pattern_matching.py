# Extract emails from emails.txt
import re

def extract_emails(inp_str):
    pat = "[a-z0-9.]+@[a-z]+\.[a-z]+" 
    return re.findall(pat, inp_str)

def readfile(fname):
    data = ''
    try: 
        with open(fname,'r') as fp:
            data = fp.read()
    except FileNotFoundError:
        print('The file you are trying to read does not exist')

    return data

if __name__ == '__main__':
    fname = input("Enter the filename to extract emails: ")
    data = readfile(fname)
    list_of_emails = extract_emails(data)
    print(list_of_emails)