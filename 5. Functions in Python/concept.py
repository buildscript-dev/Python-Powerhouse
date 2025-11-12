# Function - Reuseable block of code.
# Type of function 
# 1. UserDefine Function
# 2. InBuilt Function

def funName():
  print("Hello greeting from python")
  return "I'm Returning a value"

funName() # Calling the function

print(funName())

# Print VS Return
# Output ke liye print use krte hai.
# Values return krne ke liye


# Parameter - () where we put some variable is a parameter.
# Argurment - Is a value to the parameter.

def addition(a,b):
  print(a+b)

addition(156,123)


def pallendrome(insert):
  rev = 0
  copy = insert

  while insert > 0:
    rev = (rev * 10) + (insert % 10)
    insert = insert // 10
  
  if rev == copy:
    print("Yes, It's a pallendrome")
  else:
    print("No, It's not pallendrome")

pallendrome(121)
pallendrome(1221)
pallendrome(33333)
pallendrome(12222221111)


# Keyword argument - here we provide the specific value like d = 12, and c = 12321
def subtraction(c,d):
  print(c-d)

subtraction(d=12,c=2)

# Default parameter/ parameter with values. - giving the pararment a default value if it not given by user.
def multiplication(e,f=1):
  print(e*f)

multiplication(5)
multiplication(5,2)