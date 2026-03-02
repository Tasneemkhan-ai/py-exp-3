# AIM: Write a Python program to calculate the gross salary of an employee.
# Coder:Tasneem Khan
# Date:02-03-2026

# Write your code here
print("- Gross Salary Calculator-")
#To get base salary from user
bs=float(input("Enter your base salary:"))
print("Basic salary is",bs)
da=0.7*bs
print("Daily allowance is ",da)
ta=0.3*bs
print("Travel allowance is",ta)
hra=0.1*bs
print("House rent allowance is",hra)
gross_salary=bs+da+ta+hra 
print("Gross salary:",gross_salary)
