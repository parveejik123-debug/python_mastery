#check weather number is strong number or not 
number = int(input("Enter the number :"))
full_number = len(str(number))
temp = number

def Find_strong_number(temp):
    Final_answer = 0
    for digit in range(full_number):
        last_number = temp % 10
        fact_lastnumber = 1
        for x in range(1,last_number+1):
            fact_lastnumber = fact_lastnumber * x
        Final_answer += fact_lastnumber
        temp = temp // 10

    if Final_answer == number:
        print(f"{number} is the strong number")
    else:
        print("This is not the Strong number ")


Find_strong_number(temp)

# print the first N strong number 

number = int(input("Enter the number :"))

def Find_strong_number(number):
    for number in range(1,number+1):
        full_number = len(str(number))
        temp = number   

        Final_answer = 0
        for digit in range(full_number):
            last_number = temp % 10
            fact_lastnumber = 1
            for x in range(1,last_number+1):
                fact_lastnumber = fact_lastnumber * x
            Final_answer += fact_lastnumber
            temp = temp // 10

        if Final_answer == number:
            print(f"{number} is the strong number")
        # else:
        #     print("This is not the Strong number ")


Find_strong_number(number)


#Print the strong number between two number 

number1 = int(input("Enter the number :"))
number2 = int(input("Enter the number :"))

def Find_strong_number(number1,number2):
    for number in range(number1,number2+1):
        full_number = len(str(number))
        temp = number   

        Final_answer = 0
        for digit in range(full_number):
            last_number = temp % 10
            fact_lastnumber = 1
            for x in range(1,last_number+1):
                fact_lastnumber = fact_lastnumber * x
            Final_answer += fact_lastnumber
            temp = temp // 10

        if Final_answer == number:
            print(f"{number} is the strong number")
        # else:
        #     print("This is not the Strong number ")


Find_strong_number(number1,number2)
