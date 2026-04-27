num2 = [10, 501, 22, 37, 100, 999, 87, 351]

prime = [] # list to store prime numbers

for i in num2: # for accessing numbers in the list
    
    
    if i > 1: # prime numbers are greater than 1
        
        for j in range(2, i): # check divisibility from 2 to i-1
            
            
            if i % j == 0: # if divisible its not a prime number

                break
              
        else:  # it executes only if loop is NOT broken

            prime.append(i)   # add prime number to list

print("Prime Numbers:", prime)
print("Count:", len(prime))