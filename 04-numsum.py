# Author: Vishwas Singh
# Email: vishwasks.reach@gmail.com
#
#Take n numbers from user
# until he enters -999
# print total & average

total = 0
count = 0
while True:
    num = int(input("Enter the Number: "))
    if num == -999:
        break

    total += num
    count += 1


print(f"The sum of {count} of numbers is: {total}")
print(f"The average of {count} of numbers is: {total/count}")
