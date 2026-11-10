
# Code to check weather the number is prime number or not 
Number = int(input("Enter the number : "))

def Find_weather_number_Prime_number(Number):
    sample_number = int(Number ** 0.5)
    for digit in range (2,sample_number+1):
        if Number % digit == 0 :
            print(f"{Number} is not the prime number")
            return
        
    print(f"{Number} is the prime number")

Find_weather_number_Prime_number(Number)

#code to check Prime number upto N number

Number = int(input("Enter the number : "))

def Find_weather_number_Prime_number_upto_N(Number):
    for each_number in range(2,Number+1):
        if each_number <= 1:
            continue
        sample_number = int(each_number ** 0.5)
        for digit in range (2,sample_number+1):
            if each_number % digit == 0 :
                break
        else:
            print(f"Prime Number : {each_number}")

Find_weather_number_Prime_number_upto_N(Number)

#code to check Prime number between two number

Number1 = int(input("Enter the number1 : "))
Number2 = int(input("Enter the number2 : "))

def Find_Prime_number_between_two_Number(Number1,number2):

    for each_number in range(Number1,number2+1):
        if each_number <= 1:
            continue
        sample_number = int(each_number ** 0.5)
        for digit in range (2,sample_number+1):
            if each_number % digit == 0 :
                break
        else:
            print(f"Prime Number : {each_number}")

Find_Prime_number_between_two_Number(Number1,Number2)

