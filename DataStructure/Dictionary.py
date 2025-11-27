#key-value pair

persons={
    "name":"vaishnavi",
    "age": 24,
    "height":5.4,
    "city" : "Nagpur"

}

#added new key value pair 
persons["country"]="INDIA"

#deleting the data
del persons["country"]

#printing each item
for i, j in persons.items():
    print(f"{i}: {j}")

#printing age of the person
print(f"Age of the persons is  : {persons["age"]}")

#print(", ".join(f"{key}:{value}" for key, value in persons.items()))