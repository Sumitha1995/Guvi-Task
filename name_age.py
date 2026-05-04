detail = [ {"name" :"Vamsi" ,"age" : 31 },
            {"name":"Viyan" , "age" : 3 },              # details of the person stored in dictionary
            {"name" :"Smitha", "age" : 30} ]         

res =list(map(lambda x : x ["name"],filter(lambda x : x ["age"] >= 18 ,detail)))  # lambda function is used to filter the age >=18 and mapped the details of the person using map()

print(res)  # Names of the person is printed whose age is >18
