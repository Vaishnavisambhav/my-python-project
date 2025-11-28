def greeting(name ,institute):
    print(f"Hello {name} , Welcome to {institute}")

#name = input("Enter Your Name Here : ")
#institute = input("Enter the name of your Institute: ")

greeting(name ="Vaishnavi",institute="Sambhav")
#OR
greeting("Vaishnavi","Sambhav") #will give the same output


def greet2(first_name,last_name):
    print(f"Hello,{first_name} {last_name}")

greet2("Vaishnavi","Kaple")

#pre defined name / default first_name
def greet3(last_name,first_name="vaishnavi"):
    print(f"Hello,{first_name} {last_name}")

greet3(last_name="Kaple" , first_name="XYZ")
