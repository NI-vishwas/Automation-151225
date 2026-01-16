# Author: Vishwas Singh
# Email: vishwasks.reach@gmail.com
#

email_id = input("Enter the email id: ")
# A user name is part of email id before @ symbol

idx = -1
# for i in range(len(email_id)):
#     if email_id[i] == '@':
#         idx = i
idx = email_id.index('@')

if idx != -1:
    print(f"User name is {email_id[:idx]}")
else:
    print("The email is invalid")

k = 'vishwas singh'
k.index()



# 'vishwas k singh'
# v:1, i:2,s:3,h:2.....




