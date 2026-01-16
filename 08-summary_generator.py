# Take the file name or path from the user
# read the file
# write the summary of the file to a summary.log
# Example:
# Input filename: data.txt
# Entry in summary.log
# Summary of data.txt at 15 Jan 21.06
# ------------------------------------
# Number of Lines: 10
# Number of Words: 250
# Number of Characters: 1500
# Number of punctuations: 10
# Number of vowels: 100

import datetime
import string

SUMMARY_FILE = 'summary.log'
def readfile(fname, mode):
    try:
        with open(fname, 'r') as fp:
            if mode == '1':
                data = fp.read()
            elif mode == '2':
                data = fp.readlines()
        
        return data
    except FileNotFoundError:
        print("File does NOT EXIST")

def num_lines(fname):
    data = readfile(fname, '2')
    return len(data)

def num_chars(fname):
    data = readfile(fname, '1')
    return len(data)

def num_words(fname):
    data = readfile(fname, '1')
    return len(data.split())

def writefile(fname, data):
    with open(SUMMARY_FILE,'a') as fp:
        formatted_date = datetime.datetime.now().strftime('%d %b %H.%M')
        title = f"Summary of {fname} at {formatted_date}"
        fp.write(title+'\n')
        fp.write('-'*90+'\n')

        for k,v in data.items():
            fp.write(k+' : '+str(v)+'\n')


if __name__ == '__main__':
    fname = input('Enter the file name with path: ')
    write_data = {}
    write_data['Number of Lines'] = num_lines(fname)
    write_data['Number of Words'] = num_words(fname)
    write_data['Number of Chars'] = num_chars(fname)
    writefile(fname,write_data)