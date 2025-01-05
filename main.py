name="100"
age = 14
weight = 48.9
is_student = True

print(type(is_student))

age = bool(age)
print(age)

name = float(name)
print(name)

num1 = 100
num2 = 225
print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 * num2)
print(num2 ** 2)
print(num1 ** 0.5)
print(num1 == num2)
print(num1 > num2)
print(num2 < num1)
print(num1 != num2)

x = input("Enter value of x:")
y = input("Enter value of y:")

temp = x
y = x
y = temp

print("value of x after swapping", x)
print("value of y after swapping", y)