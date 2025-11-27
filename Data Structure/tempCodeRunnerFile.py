name = "Vaishnavi Kaple"
age = 24
height = 5.6
student = False
data_types_list =[name, age, height, student]
print(" , ".join(str(item) for item in data_types_list))  


#another method to print the items of the list in one line with comma separator
for i in range(len(data_types_list)):
    if i != len(data_types_list)-1:
        print(data_types_list[i], end = ", ")
    else: