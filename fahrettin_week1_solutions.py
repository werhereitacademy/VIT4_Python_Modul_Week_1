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


