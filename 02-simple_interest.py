# Author: Vishwas Singh
# Email: vishwasks.reach@gmail.com
# Script to find the simple interest

principal = int(input("Enter the principal: "))
time_in_months = int(input("Enter the time in months: "))
rate_of_interest = float(input("Enter the rate of interest: "))

simple_interest = (principal * time_in_months * rate_of_interest) / 100
# print(simple_interest)
# print("The Simple Interest is:",simple_interest)
# print("The Simple Interest is: "+simple_interest)
# print("The Simple Interest is: %i"%(simple_interest))
# print("The Simple Interest is: {0:.2f}".format(simple_interest))
# print("This is {0} programming version is {1}".format("python",3))
print(f"The Simple Interest is: {simple_interest:.2f}")
