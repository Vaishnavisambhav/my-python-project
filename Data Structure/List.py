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

