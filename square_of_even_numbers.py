lst = [1, 2, 3, 4, 5 ,6]    #list of numbers

res=list(map(lambda x : x*x ,filter(lambda x : x%2==0,lst))) # filter is used to get even numbers 
							     # map used to square selected numbers

print(res) # Square of even numbers is printed