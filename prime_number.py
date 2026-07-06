class prime_number:
    def __init__(self,num):
        self.num = num
    
    def check_prime_num(self):
        limit = int(self.num ** 0.5)
        is_prime = True
        if self.num <=1:
           is_prime = False
           print("not a prime")
           return 
        for i in range(2,(limit+1)):
            if self.num % i == 0:
                is_prime = False
                break

        if is_prime:
         print("Prime")
        else:
         print("Not Prime")

p1 = prime_number(17)

p1.check_prime_num()