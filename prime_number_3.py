def prime_number(num1,num2):
    if num1 > num2:
        print("Not the valid menthod of checking prime number between two numbers ")

    if num1 < 1:
        num1 = 2

    for i in range(num1,num2+1):
        is_prime = True
        limit = int(i ** 0.5) + 1

        for j in range(2,limit):
            if i % j ==0:
                is_prime = False
                break
            else:
                is_prime= True 
        
        if is_prime:
            print(i)

prime_number(-5,10)
