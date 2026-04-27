lst = [4, 2, -3, 1, 6]

n = len(lst)

found = False   # Flag to check if sublist is found

for i in range(n): #starting index of sublist

    total = 0
    
    for j in range(i, n): #extend sublist from i to end

        total += lst[j]   # Add current element to total
        
        
        if total == 0: # Check if sum becomes zero
            print("Sublist:", lst[i:j+1])  # Print the sublist
            found = True   # Mark as found
            break          # Stop inner loop
    
    if found:
        break   # Stoping loop if sublist already found

if not found: # If no sublist
    print("No sublist found")