# Assignment:
# Take your payroll program from chapter 2 and make it better.
# Remember to start with a comment with your name, date, and title of the program
# Add an if-else conditional structure to calculate overtime pay for all hours worked over 40. That means 1.5 times the hourly pay for each hour over 40, so if you work 45 hours and your hourly pay is $10, you get $10 an hour for the first 40, and $15/hr for the next 5.
# Add simple error handling so that if the user enters a text string when you're expecting a number, it will display a nice message instead of an ugly error.

# Getting date on employee one
name1 = input('Please enter an employee name: ')
hour1 = input('Hours worked: ')

# Make sure input is correct value type
try:
  hourint1 = int(hour1)
except ValueError:
  print("You need to input a number for the hours!")
  raise SystemExit
  
wage1 = input('Hourly wage: ')
try:
  wageint1 = int(wage1)
except ValueError:
  print("You need to input a number for the wage!")
  raise SystemExit
print(" ")

# Employee one gross pay calculation
if hourint1 > 40:
  nonovertimewage1 = 40*wageint1
  overtimehours1 = hourint1-40
  overtimewage1 = overtimehours1*1.5*wageint1
  wage1 = overtimewage1+nonovertimewage1
else:
  wage1 = hourint1*wageint1

# Getting date on employee two
name2 = input('Please enter a second employee name: ')
hour2 = input('Hours worked: ')

# Makes sure input is correct value type
try:
  hourint2 = int(hour2)
except ValueError:
  print("You need to input a number for the hours!")
  raise SystemExit
  
wage2 = input('Hourly wage: ')

try:
  wageint2 = int(wage2)
except ValueError:
  print("You need to input a number for the wage!")
  raise SystemExit
print(" ")

# Employee two gross pay calculation
if hourint2 > 40:
  nonovertimewage2 = 40*wageint2
  overtimehours2 = hourint2-40
  overtimewage2 = overtimehours2*1.5*wageint2
  wage2 = overtimewage2+nonovertimewage2
else:
  wage2 = hourint2*wageint2

# Last responce (sends data)
print(f"{name1}'s gross pay is ${str(wage1)}")
print(f"{name2}'s gross pay is ${str(wage2)}")
inbank = wage1+wage2
print(f"Make sure you have ${str(inbank)} in the bank!")

# Comment with name, date, and assignment name redacted
