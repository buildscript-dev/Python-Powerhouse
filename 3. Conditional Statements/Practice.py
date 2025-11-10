# -------------------------------------------
# Question 1. Check whether number is greater.
# -------------------------------------------
# a = float(input("Enter your first number: "))
# b = float(input("Enter your second number: "))
#
# if a > b:
#     print(f"{a} is greater than {b}")
# elif b > a:
#     print(f"{b} is greater than {a}")
# else:
#     print(f"both {a} and {b} is equal")


# -------------------------------------------
# Question 2. Check whether person is "M/F"
# -------------------------------------------
# userInput = input("Enter M/m or F/f: ")
#
# if userInput == "M" or userInput == "m":
#     print("Sir are Male.")
# elif userInput == 'F' or userInput == 'f':
#     print("Mam are Female.")
# else:
#     print("Either you're LGBTQ")
#     print("OR")
#     print("Invalid Prompt")


# -------------------------------------------
# Question 3. Check whether number is Even or Odd.
# -------------------------------------------
# userInput = int(input("Enter your number: "))
#
# if userInput % 2 == 0:
#     print(f"{userInput} is Even.")
# else:
#     print(f"{userInput} is Odd.")


# -------------------------------------------
# Question 4. Check whether person can vote with name and age and tell when person can vote.
# -------------------------------------------
# userName = input("Enter your name: ")
# userAge = int(input("Enter your age: "))
#
# if userAge >= 18:
#     print(f"{userName} you are {userAge} year old, You can vote.")
# elif userAge <= 17:
#     print(f"You cann't vote now, but you can vote after {18-userAge} year.")
# else:
#     print("Invalid Input.")


# -------------------------------------------
# Question 5. Check whether number is greatest among 3.
# -------------------------------------------
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
#
# if a == b and b == c:
#     print("All the numbers are equal.")
# elif a == b or b == c or c == a:
#     print(f"Any two number is equal.")
# elif a > b and a > c:
#     print(f"{a} is greater.")
# elif b > a and b > c:
#     print(f"{b} is greater.")
# elif c > a and c > b:
#     print(f"{c} is greater.")
# else:
#     # print("Invalid Input")
#     pass


# -------------------------------------------
# Question 6. Check whether number is Leap Year.
# -------------------------------------------
# userInput = int(input("Enter the year: "))
#
# if userInput % 100 == 0 and userInput % 400 == 0:
#     print(f"{userInput} is Leap year.")
# elif userInput % 100 != 0 and userInput % 4 == 0:
#     print(f"{userInput} is Leap year.")
# else:
#     print(f"{userInput} is not a Leap year.")


# -------------------------------------------
# Question 7. Check whether eligible for discount.
# -------------------------------------------
# userInput = int(input("Enter you bill amount: "))
#
# if userInput >= 1000 and userInput <= 10000:
#     print("You get 10% discount")
#     print((userInput * 90) / 100)
#     print("Visit Soon...")
# elif userInput <= 1000:
#     print("You get 5% discount.")
#     print("But in next visit.")
# else:
#     print("Sorry, No discount for you.")


# -------------------------------------------
# Question 8. Check whether letter is vowel or consonant.
# -------------------------------------------
# userInput = input("Enter a letter: ")
#
# if userInput in "aeiouAEIOU":
#     print(f"{userInput} is an vowel.")
# else:
#     print(f"{userInput} is consonent.")


# -------------------------------------------
# Other Practice set
# -------------------------------------------
# userInput = int(input("Enter your number: "))


# Question 1. Check whether number is positive, negative or zero.
# if userInput >= 1:
#     print(f"{userInput} is Positive.")
# elif userInput == 0:
#     print(f"{userInput} is Zero.")
# elif userInput <= -1:
#     print(f"{userInput} is Negative.")
# else:
#     print("Invalid input.")


# Question 2. Check whether person is eligible to vote.
# if userInput >= 18 and userInput <= 150:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")


# -------------------------------------------
# Question 3. Check where string is found or not.
# -------------------------------------------
# userInput = input("Enter you string.")

# # if userInput in "aA": "This help is only single character" failer if you check for a word
# if "a" in userInput or "A" in userInput:
#     print("a found")
# else:
#     print("a not found")
