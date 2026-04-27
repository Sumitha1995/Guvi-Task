lst = [10, 20, 30, 9] 
target = 59

n=len(lst) # to find the length of the list

for i in range(n): #accessing 1st number in the list

    for j in range(i+1,n): #accessing 2nd number in the list and addition is done

        for k in range(j+1,n): #accessing 3rd number in the list and addition is done


            if lst[i] + lst[j] + lst[k] == target : #comaring the list values with target

                print("Triplet values in the list are :",lst[i],lst[j],lst[k])
