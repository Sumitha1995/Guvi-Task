lis1 = [1,2,3,4,5]
lis2 = [5,8,7,1,6]
lis3 = [9,10,1,5,14]

duplicate = [] #List to store duplicate values

for i in lis1: #access the elements in list1
    if i in lis2 and i in lis3: #comparing the values in lis2 and lis3 with value of lis1
        duplicate.append(i) #adding elements to duplicate list

print("Duplicates:", duplicate) #printing the duplicate values