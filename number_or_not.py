word = "123"

res = (len(list(filter(lambda x: x.isdigit(), word))) == len(word)) # Used to filter the digits from string

print(res)

