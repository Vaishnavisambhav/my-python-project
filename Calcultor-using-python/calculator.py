def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        return"Error, cannot divide by 0"
    return a/b
dash = (10 * "=")

while True:
    print(f"{dash }Simple Calculator {dash}")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter the choice (1-5) : ")


    if choice =="5":
        print("Thank You! Exiting Calculator ")
        break

    if choice not in ("1","2","3","4"):
        print("Invalid Choice ")
        continue

    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number : "))

    if(choice == "1"):
        print ("The addition of the numbers is :" , add(num1,num2))

    elif(choice == "2" ):
        print("the substraction of the numbers is : " , sub(num1,num2))

    elif(choice == "3" ):
        print("the substraction of the numbers is : " , mul(num1,num2))

    elif choice == "4":
        print("Result:", div(num1, num2))

