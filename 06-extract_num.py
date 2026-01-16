# Author: Vishwas Singh
# Email: vishwasks.reach@gmail.com
# Extract numbers from given string
# and print their sum

inp_str = "The mangoes cost me 20 rupees & apples cost me 200 rupees"
nums = []
for item in inp_str.split():
    if item.isdigit():
        nums.append(int(item))
    else:
        continue

print(f"Total: {sum(nums)}")
