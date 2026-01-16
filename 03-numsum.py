# Author: Vishwas Singh
# Email: vishwasks.reach@gmail.com
# Given 10 numbers from user
# Calculate their sum & average

total = 0
for i in range(10):
    num = float(input("Enter the number: "))
    total += num


avg = total / 10
print(f"The sum of 10 nos is: {total}")
print(f"The average of 10 nos is: {avg}")
