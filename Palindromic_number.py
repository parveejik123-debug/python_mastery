#code to find the palindromic number 

Number = int(input("Enter thr number : "))

def Find_palindromic_number(Number):
    len_number = str(Number)
    Sample = Number
    reverse = 0
    for _ in len_number:
        last_digit = Sample % 10
        reverse = (reverse * 10) + last_digit 
        Sample = Sample // 10
    if Number == reverse:
        print(f"{Number} This is the palindromic number")
    else:
        print(f"{Number} This is not the palindromic number")

Find_palindromic_number(Number)

# code to find the N palindromic number 

Number = int(input("Enter the palindromic number : "))

def Find_palindromic_number_For_N_number(Number):
    for digit in range(1,Number+1):
        len_number = str(digit)
        temp_number = digit
        reverse = 0
        for _ in len_number:
            last_digit = temp_number % 10 
            reverse = (reverse * 10) + last_digit
            temp_number = temp_number // 10 
        if reverse == digit:
            print(digit)

Find_palindromic_number_For_N_number(Number)

# code to find the palindromic number between two number

Number1 = int(input("Enter the first  number : "))
Number2 = int(input("Enter the secound  number :"))

def Find_palindromic_number_For_N_number(X,Y):
    for digit in range(X,Y+1):
        len_number = str(digit)
        temp_number = digit
        reverse = 0
        for _ in len_number:
            last_digit = temp_number % 10 
            reverse = (reverse * 10) + last_digit
            temp_number = temp_number // 10 
        if reverse == digit:
            print(digit)

Find_palindromic_number_For_N_number(Number1,Number2)

