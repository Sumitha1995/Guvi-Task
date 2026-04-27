num1 = [10,501,22,37,100,999,87,351]

even=[] # create empty lists to store even numbers
odd=[] # create empty lists to store odd numbers

for i in num1 : # for accessing each numbers in the list

    if i%2==0 : # To check number is even

        even.append(i) #To add even numbers in the list
    else :
        odd.append(i) #To add odd numbers in the list

print("Even List :",even)
print("Odd List :",odd)