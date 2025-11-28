def double_value(number):
    result = number *2
    return result


number = int(input("Enter the number : "))
number2 = int(input("Enter the number 2 : "))
total  =double_value(number) + double_value (number2)
print(f"The total of the number is : {total}")

if total>999:
    print("Result has 4 Digit number")
elif total>99:
    print("Result has 3 Digit number")
else:
    print("Result has 2 Digit number")
