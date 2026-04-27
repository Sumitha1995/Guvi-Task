num=int(input("Enter Number : "))

last_digit= num%10 # To get the last digit

while num >= 10: # loop to reduce the number to get the last digit

    num=num//10	# To remove last digit

first_digit = num

print("Sum of Two Numbers is",first_digit + last_digit)