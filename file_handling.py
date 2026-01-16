
# fp = open('data.txt')
# # data = fp.read()
# data = fp.readlines()
# print(data)

data = {
    "name":"vishwas",
    "email":"vishwas@gmail.com"
}
# Truncates the file (destructive)
# fp = open('test1.txt','w')
#fp = open('test2.txt','x')
# fp = open('test1.txt','a')
# fp.write(data['email'])
# fp.close()

# Handling resources using context manager
# with open('test1.txt','w') as fp:
#     fp.write(data['email'])

# Exception Handling
try:
    with open('test1.txt','w') as fp:
        fp.write(data['email'])
    with open('test3.txt','r') as fp:
        print(fp.read())

except FileExistsError:
    print("The file you are trying to write exists")

except FileNotFoundError:
    print("The file you are trying to read does not exist")

except Exception:
    print("Internal Error Occured")

else:
    print('Else')

finally:
    print("Reset the previous computations")

# For-else
# Switch
# while else