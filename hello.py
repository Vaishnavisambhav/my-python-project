"""
first_name = "vaishnavi"
last_name = "kaple"
student_age = 24 

long_dash = "-" * 25
long_space = " " * 5
full_name = first_name + " " + last_name

length= len(full_name)

print(long_dash  + "\n" + long_space+full_name+long_space  + "\n" +  long_dash)
print("length of the name is : " , length)

age = 18 
student_age = int(input("Enter your age: "))


if student_age >= age:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
"""

score = 5

score+= 10

print(score)

name ="vaishnavi Kaple"

string = f"my name is {name}"

print(string)