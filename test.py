import math

tic ='QAN.AX'
print(tic)


str1 = "What's good?"
print(str1)

str3 = '''John said: "Let's learn Python together"“.'''
print(str3)

i = 1
test = i==1
print(test)

j = 0.2+0.2+0.2
test1 = j == 0.6
print(test1)
print(Math.isclose(j,0.6))

weird_case = "My fUnNy tYpEcAsE sTrInG"
weird_case_lower = weird_case.lower()
print(weird_case_lower)

x = str('abc')
xup = str.upper(x)
print(xup)

a = True
b = 5
print("The value of a is {a} and the value of b is {b}")

x = str(5)
print(x) # --> '5'

# Create a variable called "str", overwriting the built-in method
str = "very bad idea!"

del (str)
# Trying to use the function `str` again will raise an exception
x = str(5)
print(x)

Length = 56
Width = 33
height = 30.5
Volume_of_box= Length * Width * height
print(Volume_of_box)
print("the volume of this box is {} cubic centimeters".format(Volume_of_box))