lis1 = [1,2,3,5,6,5,5] #list of numbers

for i in lis1: #accessing numbers in the list

    if lis1.count(i) == 1: # Check current element appears only once in the list

        print("First non-repeating element:", i)

        break