#class Prime_No(object):

def is_prime_number(num):
    prime_numbers = []

    if num < 2:
        return False

    if type(num) != int:
        return "Must be an integer"

    for i in range(2, num +1):
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
            prime_numbers.append(i)
    return prime_numbers

print is_prime_number(23)

                    
       
            
            
            
            
            
            
            
            
            
            
            
            

