first_name = "vaishnavi"
last_name = "kaple"
age = 24
height = 5.6
is_student = False

my_list = [first_name, last_name, age, height, is_student] 

for i in range(len(my_list)):
    print(",".join(str(i) for i in my_list))