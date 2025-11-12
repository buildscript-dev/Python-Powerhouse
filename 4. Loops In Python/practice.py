# Question 1. Print "Hello World" n times.

# n = int(input("Enter value of n: "))

# for i in range(n):
#   print("Hello World")


# Question 2. Print number from 1 to n.

# n = int(input("Enter value of n: "))

# for i in range(1,n+1):
#   print(f"{i}")

# Question 3. Print number from n to 1.

# n = int(input("Enter number: "))

# for i in range(n,0,-1):
#   print(f"{i}")

# Question 4. Sum of Natural Numbers (1 to n).

# n = int(input("Enter the number: "))

# s = 0

# for i in range (1,n+1,1):
#   print(f"{i}: {s + i}")
#   s = s + 1

# Question 5. Factorial of a Number.

# n = int(input("Enter the number: "))

# fact = 1

# for i in range(n, 0,-1):
#   print(f"{i}: {fact * i}")
#   fact = fact * i

# Question 6. Sum of Even & Odd Number in Range.

# n = int(input("Enter the number: "))

# evenStore = 0
# oddStore = 0

# for i in range(1, n+1, 1):
#   if i % 2 == 0:
#     evenStore = i + evenStore
#   else:
#     oddStore = i + oddStore
# print(f"Your total Even is {evenStore} and Odd is {oddStore}")    


# Question 7. Print All Factors of a Number.

# n = int(input("Enter the number: "))

# for i in range(1, n+1, 1):
#   if n % i == 0:
#     print(f"{i} is Factorinal.")
#   else:
#     pass

# Question 8. Sum of All Factors.

# n = int(input("Enter the number: "))
# s = 0

# for i in range(1, n+1, 1):
#   if n % i == 0:
#     s = s + i

# print(f"The sum is {s}")

# Question 9. Power Calculation (a^b)

# a = int(input("Enter the number: "))
# b = int(input("Enter the exponential: "))

# power = a

# for i in range (b):
#   a = power*a
# print(f"The power of {power} to the power {b} is {a}")


# While Loop

# Question 1. Print Number in reverse order.

# n = int(input("Enter a number: "))

# while n != 0:
#   if n > 0:
#     print(f"{n}")
#     n = n - 1
    
#   elif n < 0:
#     print(f"{n}")
#     n = n + 1
#   else: 
#     print(f"Invalid Input {n}")\
    

# Question 2. Print Each Digit in reverse order

# n = int(input("Enter your number: "))

# while n > 0:
#   print(n % 10)
#   n = n // 10

# Question 3. Print Sum of Digit

# n = int(input("Enter your number: "))

# store = 0

# while n > 0:
#   store = store + n % 10
#   n = n // 10

# print(f"Total sum is {store}")

# Question 4. Reverse a Digit.

# n = int(input("Enter a number: ",))

# while n > 0:
#   print(f"{n%10}", end="")
#   n = n // 10

# Question 5. Parendromic Number

# n = int(input("Enter any number: "))
# preValue = n
# rev = 0

# while n > 0:
#   rev = rev * 10 + n % 10
#   print(f"rev", end="")
#   n = n //10

# print("")

# if preValue == rev:
#   print(f"Yes, {preValue} is a Parendromic number.")
# else:
#   print(f"No, {preValue} is not a Parendromic number.")

# Question 6. Automorphic number

n = int(input("Enter a number: "))

square = n ** 2
