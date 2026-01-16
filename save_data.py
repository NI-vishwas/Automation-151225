# import utils
from lib.utils import uname_extracter
# given a email id 
email = input("Enter the email Id: ")

# extract the username 
#username = utils.uname_extracter(email)
username = uname_extracter(email)

# save to database
print(f"{username} is extracted from {email} and saved to db")
