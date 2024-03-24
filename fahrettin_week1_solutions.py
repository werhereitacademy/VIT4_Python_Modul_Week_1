#Soru 1 :
count = 1
print("Integers from 1 to 10 :")
while count < 11:
    print(count, end="  ")
    count += 1
  
print("\n--------------------------")

#Soru 2 :
number = int(input("Enter a number: "))

# Using foor loop
print("Even numbers up to", number, "using for loop:")
for i in range(0, number+1, 2):   
    print(i, end=" ")

print("\n")
# Using while loop
print("Even numbers up to", number, "using while loop:")
j = 0
while j <= number:
    if j % 2 == 0:
        print(j, end=" ")
    j += 1

print("\n--------------------------")

#Soru 3:
first_number = int(input("Enter the first number: "))
last_number = int(input("Enter the last number: "))
print(f"Numbers between {first_number} and {last_number} (inclusive):")
for i in range(first_number, last_number+1):
    print(i, end="  ")

print("\n-------------------------")

#Soru 4 :
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
  
print("\n-------------------------")

#Soru 5:
number = int(input("Enter a positive number: "))
user_number = number
factorial = 1
while number > 0 :
    factorial *= number
    number -= 1
print("Factorial of {} is: {}".format(user_number, factorial))

print("\n-------------------------")

#Soru 6:
number = int(input("Enter a number: "))

if number > 1:
    divisor = 2
    is_prime = True
    
    while divisor <= number ** 0.5  :
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")
else:
    print(number, "is not a prime number")

print("\n-------------------------")

#Soru 7:
limit = 100
fibonacci_list = [0, 1]

while True:
    next_fibonacci = fibonacci_list[-1] + fibonacci_list[-2]
    if next_fibonacci > limit:
        break
    fibonacci_list.append(next_fibonacci)
print(f"Fibonacci sequence up to {limit} is: {fibonacci_list}")

print("\n-------------------------")

#Soru 8:
word = input("Enter a word: ")
reversed_word = ""
for letter in word:
    reversed_word = letter + reversed_word
print("Reversed word is", reversed_word)

print("\n-------------------------")

#Soru 9:
word = input("Enter a word: ")
first_index = 0
last_index = -1
is_polindrome = True

while first_index < len(word) / 2:
    if word[first_index] != word[last_index]:
        is_palindrome = False
        break
    
    first_index += 1
    last_index -= 1

if is_palindrome:
    print(word, "is polindrome")
else:
    print(word, "is not polindrome")

# or in short  
if word == word[::-1]: 
    print(word, "is polindrome") 
else:
    print(word, "is not polindrome")

print("\n-------------------------")

#Soru 10:
height = float(input("Your height in meter: "))
weight = float(input("Your weight in kilograms: "))
# BMI(Body Mass Index)
bmi = ((weight * 10) // height ** 2) / 10  # to display only two decimal places

if bmi < 25:
    category = "underweight"
elif bmi < 30:
    category = "normal"
elif bmi < 40:
    category = "overweight"
else:
    category = "obese"

print(f"Your body mass index is {bmi}  You are {category}")

print("\n-------------------------")

#Soru 11
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest_num = num1
if num2 > largest_num:
    largest_num = num2

if num3 >largest_num:
    largest_num = num3

print("The largest number is:", largest_num)

# or
num_list = [num1, num2, num3]
print("The largest number is:", max(*num_list))
print("The largest number is:", max(i for i in num_list))
print("The largest number is:", sorted(num_list)[-1])

print("\n-------------------------")

#Soru 11
courses = ["Math", "Physics", "Chemistry", "Biology"] 

for i in courses:
    print("For the course", i)
    midterm = int(input("Enter the midterm score: "))
    final = int(input("Enter the final score: "))

    average = midterm * 0.4 + final * 0.6

    if average < 50:
        print("Fail")
    else:
        print("Pass")
