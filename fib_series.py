n = 5  #number of terms to print

a, b = 0, 1 #first two fibonacci numbers

fib = lambda x, y: (y, x + y) #lambda function to generate next pair

for i in range(n):
    print(a, end=" ") #Prints current fibonacci series
    a, b = fib(a, b) #update value