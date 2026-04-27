list1 = [10, 501, 22, 37, 100, 999, 87, 351]

def is_happy(num): # function to check number is happy number or not

    while num != 1 and num != 4: #loop until number becomes 1 and 4
        total = 0

        while num > 0: # find sum of squares of digits

            digit = num % 10 # To get last digit
            total += digit * digit # Square and addition
            num = num // 10 # Removes last digit

        num = total
    return num == 1  # Return True if happy, else False


happy_numbers = []
count = 0

for i in list1 :

    if is_happy(i):  # check if the number is happy

        happy_numbers.append(i)
        count += 1

print("Happy numbers:", happy_numbers)
print("Count:", count)