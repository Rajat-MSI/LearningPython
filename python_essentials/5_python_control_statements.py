# python control statements

# * types of conditional statements
# if statement
print("* if statement")
age = 18
if age >= 18:
    print("you are eligible to vote")

# if-else statement
print("\n* if-else statement")
age = 15
if age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

# nested if statement
print("\n* nested if statement")
password = "password1234"
if len(password) >= 8:
    if any(char.isdigit() for char in password):
        print("strong password")
    else:
        print("password should contain a number")
else:
    print("password is too short")

# if-elif statement
print("\n* if-elif statement")
temperature = 10
if temperature >= 30:
    print("it is hot")
elif 25 >= temperature >= 15:
    print("it is normal")
else:
    print("it is cold")


# * python loops
# for loop
print("\n* for loop")
numbers = [4,5,2,3,1,8]
squares = []
for i in numbers:
    square = i ** 2
    squares.append(square)
print("list of square numbers:", squares)

# range() function
# it is use to produce series of numbers like range(10) will produce numbers
# between 0 and 9 (10 numbers)
# range(start,stop,step size)
print("\nprinting table of 12")
for i in range (1,11,1):
    print("12 x", i,"=",i*12)

print("\niterating over list using index")
p_list = ["python","java","cpp","perl"]
for i in range(len(p_list)):
    print(p_list[i].upper())

print("\niterating over a string")
p_string = "python_programming"
for i in p_string:
    print(i,end=" ")
print()

# while loop
print("\n* while loop")
count = 0
while count < 10:
    print(count, end=" ")
    count += 1
print()

# * loop control statements
print("\n* loop control statements")
# continue - skips current iteration on given condition
print("continue statement")
p_string = "python_programming"
for i in p_string:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        continue
    print(i,end=" ")

# break - breaks loop on given condition
print("\nbreak statement")
count = 0
while count < 10:
    if count == 5:
        break
    print(count,end=" ")
    count += 1

# pass - The pass statement is used as a placeholder for future code.
print("\npass statement")
size = 5
for i in range(size):
    pass