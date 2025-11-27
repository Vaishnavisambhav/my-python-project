n = int(input("Enter how many terms of fabonacci series you want : "))
first=0
second=1

for i in range(n):
    print(first , end =" ")
    temp=first+second
    first=second
    second=temp