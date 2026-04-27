lst = [1, 2, 3, 4, 5] #original list

k = 2 # Rotate the list by 2

rotated = lst[k:] + lst[:k]

print("Rotated list:", rotated) # printing the rotated list

min_val = rotated[0] # Find minimum number

for i in rotated:
    if i < min_val:
        min_val = i

print("Minimum element:", min_val) # Print the minimum number