#List can have multiple Data types
my_list =["vaishnavi", 24, 5.6, True]

print(" , ".join(str(item) for item in my_list))


name = "Vaishnavi Kaple"
age = 24
height = 5.6
student = False
data_types_list =[name, age, height, student]

#One way to print the items of the list in one line with comma separator
print(" , ".join(str(item) for item in data_types_list))  

#another method to print the items of the list in one line with comma separator
for i in range(len(data_types_list)):
    if i != len(data_types_list)-1:
        print(data_types_list[i], end = ", ")
    else:
        print(data_types_list[i])


#list of fruits
fruits = ["Apple", "Banana", "Mango", "Orange"]

#adding the single item at end of the list
add_item=fruits.append("Grapes")

#adding multiple items at end of the list
add_items = fruits.extend(["Pineapple", "Watermelon"])

#inserting item at specific index
insert_item = fruits.insert(2, "Strawberry")

#removing item from the list
remove_item = fruits.remove("Banana")

#popping item from the list
popped_item = fruits.pop()      #removes last item

#length `of the list`
length = len(fruits)
print("Length of the list is: ", length)

#printing all items in the list
for i in range(length):
    print(fruits[i])

