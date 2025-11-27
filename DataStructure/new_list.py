first_name = "vaishnavi"
last_name = "kaple"
age = 24
height = 5.6
is_student = False

my_list = [first_name, last_name, age, height, is_student] 
print("Orginal List is : " , end = " ")
print(" , ".join(str(i) for i in my_list))

updating_at_first = my_list[0] = "Jatin"

print("Updated List is : " , end = " ")
print(" , ".join(str(j) for j in my_list))
