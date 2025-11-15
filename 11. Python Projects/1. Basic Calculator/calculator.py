# Welcome / Greet
def Basic_Calculator():
  print("Welcome to Basic Calculator....")
  print("Only use number and mathematical operators...")

  number_first = float(input("Enter number: "))

  while True:
    operator = input("Enter the operation (+, -, *, /, %), or 'q'/' ' to quit: ")

    if operator == "q" or operator == " ":
      print("Calculator closed.")
      break

    number_second = float(input("Enter number: "))

    if operator == "+":
      number_first = number_first + number_second
    elif operator == "-":
      number_first = number_first - number_second
    elif operator == "*":
      number_first = number_first * number_second
    elif operator == "/":
      if number_second == 0:
        print("Division of zero is not allowed!")
        continue
      number_first = number_first / number_second
    elif operator == "%":
      number_first = number_first % number_second
    else:
      print("Invalid Input... Try again")
      continue

    if number_first.is_integer():
      print(f"Current Total: {int(number_first)}")
    else:
      print(f"Current Total: {number_first}")

  # final output
  if number_first.is_integer():
    print(f"Your final answer is {int(number_first)}")
  else:
    print(f"Your final answer is {number_first}")


Basic_Calculator()
