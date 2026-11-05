# print the fibonacci sequence upto a given number
num = int(input("Enter the number :"))

a = 0
b = 1

for i in range(num):
    if a > num:
        break
    print(a)
    a, b = b, a + b

print("print the fibonacci sequence upto a given number successfully completed")
# print the first n fibonacci number
num = int(input("Enter the number :"))

a = 0
b = 1

for i in range(num):
    print(a)
    a, b = b, a + b

print("print the first n fibonacci number successfully completed")

# print all fibonacci between two numbers
num1 = int(input("Enter the number1 :"))
num2 = int(input("Enter the number2 :"))

a=0
b=1
for i in range(num1,num2+1):
    if num1 <= a <=num2:
        print(a)
    a,b=b,a+b

print("print all fibonacci between two numbers success fully completed ")