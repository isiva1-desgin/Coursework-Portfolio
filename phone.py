'''
Programs Name: phone.py
Author: Ishan Sivamaran Rajesh
Description: ask user for input of phone number than output
area code,  prefix, line number. 
'''

number = int(input("Please enter your phone number: "))
print()

num1 = number%10000

num2 = (number%10000000)//10000

num3 = (number%10000000000)//10000000

print(f"Phone Number: ({num3}) {num2}-{num1}")
