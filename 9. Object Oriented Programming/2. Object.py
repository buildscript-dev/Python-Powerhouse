# Object - We use class blueprint to make an object . like using the material given


class Factory:
  a = 1234
  def hello():
    print("Hello, I'm a method")

obj_greet = Factory() # Object become an object who can access anything of the class

print(obj_greet.a)
obj_greet.hello()