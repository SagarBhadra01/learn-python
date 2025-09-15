#if statement
age = 20
if age >= 18:
    print("Eligible to vote.")
    
#if-else statement
age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")
    
#elif statement
age = 25
if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")
    
#nested if-else statement
age = 70
is_member = True
if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")
    
#ternary conditional statement
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)

#match-case statement
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

#standof statement
a = 2
b = 330
print("A") if a > b else print("B")