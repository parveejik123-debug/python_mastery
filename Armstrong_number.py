# this is to check weather given number is Arm strong number or not 
num = int(input("Enter the number : "))

temp = num
questiant = len(str(num))
# print(questiant)

def Find_Armstrong_number(temp):
    total = 0 
    for i in range(questiant):
        last_number = temp % 10
        total += last_number ** questiant
        temp = temp // 10 

    if total == num:
        print("This is the Armstrong number")
    else:
        print("This is not a Armstrong number")


# Find_Armstrong_number(temp)

Frint the  First N Arm strong number

num = int(input("Enter the  number : "))


def Find_Armstrong_number_upto_N(num):
    for digit in range(1,num+1):
        questiant = len(str(digit))
        temp = digit
        total = 0

        for _ in range(questiant):
            last_number = temp % 10
            total += last_number ** questiant
            temp = temp // 10
        if total == digit:
            print(digit)

Find_Armstrong_number_upto_N(num)

# Find the Arm strong number between two numbers

number1 = int(input("Enter the number 1 : "))
number2 = int(input("Eneter the number 2 : "))

def Find_ArmStrong_number_betweeb_two_numbers(number1,number2):
    for digit in range(number1,number2):
        questiant = len(str(digit))
        temp = digit
        total = 0
        for _ in range(questiant):
            last_number = temp % 10
            total += last_number ** questiant
            temp = temp // 10
        if digit == total:
            print(digit)

Find_ArmStrong_number_betweeb_two_numbers(number1,number2)