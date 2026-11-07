
# Program to find the Perfect Number 

number = int(input("Enter the number : "))


def Find_the_Perfect_Number(number):
    total = 0
    for N in range(1,number):
        if number % N == 0:
            total += N

    if total > 0 and total == number:
        print("This is the perfect Number ")
    else :
        print("This is not the prime number")

Find_the_Perfect_Number(number)

# Code to Find first N Perfect Number

number = int(input("Enter the number : "))

def First_N_perfect_Numbers(number):
    for digit in range(1,number+1):
        total = 0

        for N in range(1,digit):
            if digit % N == 0:
                total += N

        if total > 0 and total == digit:
            print(digit)

First_N_perfect_Numbers(number)

# code to find perfect numbers between two numbers

number1 = int(input("Enter the first number : "))
number2 = int(input("Enter the secound number : "))

def Find_perfect_Numbers_between_two_numbers(number1,number2):
    for digit in range(number1,number2+1):
        total = 0

        for N in range(1,digit):
            if digit % N == 0:
                total += N

        if total > 0 and total == digit:
            print(digit)

Find_perfect_Numbers_between_two_numbers(number1,number2)

