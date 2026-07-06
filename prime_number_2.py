def prime_number(num):
    # print(limit)
    if num <= 1:
        is_prime = False
        print("Not a prime number")
    for i in range(2,num):
        is_prime = True
        limit = int(i ** 0.5)

        for j in range (2,(limit+1)):
                if i % j == 0:
                    is_prime = False
                    break
                else:
                    is_prime = True
        if is_prime:
             print(i)

prime_number(100)
            

            
