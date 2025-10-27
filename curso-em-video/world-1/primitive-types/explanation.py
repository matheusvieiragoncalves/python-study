# int -> number 1, 2, 3, -5, 0
# float -> number with decimal 1.5, -0.5, 3.14
# str -> letters, words, text ... "hello", 'world'
# bool -> True or False

print('\n### Checking types ###')
print(type(1))        # int
print(type(1.5))      # float
print(type("hello"))  # str
print(type(True))     # bool

print('\n### Converting between types ###')
print(int(1.5))       # 1
print(float(2))       # 2.0
print(str(100))       # "100"
print(bool(""))       # False

print('\n### boolean conversions ###')
print(bool(1))
print(bool(0))
print(bool("hello"))
print(bool(""))

print('\n### verify if possible conversions ###')
a = "123"
print(a.isnumeric())  # True

b = "hello"
print(b.isnumeric())  # False

c = '3a'
print(c.isnumeric())  # False
print(c.isalnum())    # True
