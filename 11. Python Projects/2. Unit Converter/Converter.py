# 2. **Unit Converter** — convert units (length, weight, temperature) with interactive prompts. (modules: none)

def Converter():
  print("Welcome to Unit Converter....")
  print("Here you can convert units.... ")

  value = float(input("Enter only the number: "))
  old_unit = input("Enter unit of your number(cm, m, km, g, kg, c, f): ").lower()

  while True:
    new_unit = input("Enter new unit you want to convert to: ").lower()

    # LENGTH
    if old_unit == "cm" and new_unit == "m":
      value = value / 100

    elif old_unit == "m" and new_unit == "cm":
      value = value * 100

    elif old_unit == "m" and new_unit == "km":
      value = value / 1000

    elif old_unit == "km" and new_unit == "m":
      value = value * 1000

    elif old_unit == "cm" and new_unit == "km":
      value = value / 100000

    elif old_unit == "km" and new_unit == "cm":
      value = value * 100000


    # MASS
    elif old_unit == "g" and new_unit == "kg":
      value = value / 1000

    elif old_unit == "kg" and new_unit == "g":
      value = value * 1000


    # TEMPERATURE
    elif old_unit == "c" and new_unit == "f":
      value = (value * 9/5) + 32

    elif old_unit == "f" and new_unit == "c":
      value = (value - 32) * 5/9


    # FALLBACK
    else:
      print("This conversion is not available right now.")
      break

    print(f"We have converted this into {value}{new_unit}")
    break


Converter()
