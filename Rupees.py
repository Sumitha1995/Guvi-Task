count = 0

for one in range(0,11):     # loop for number of Rs.1 coins (0 to 10)
    for two in range(0,7):  # loop for number of Rs.1 coins (0 to 7)
        for five in range(0,3):  # loop for number of Rs.1 coins (0 to 3)
            for ten in range(0,2):  # loop for number of Rs.1 coins (0 to 2)
                
                total = one*1 + two*2 + five*5 + ten*10  # calculates total value of the combinations

                if total == 10:  # checks for total if its equals to Rs.10

                    count += 1

                    print(one, two, five, ten) # prints the combination

print("Total ways:", count) # prints the count