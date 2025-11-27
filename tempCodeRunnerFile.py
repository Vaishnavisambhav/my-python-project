name ="Vaishnavi Kaple"

dash = "-" * 50

upper_case=name.upper()
lower_case=name.lower()
title=name.title()

print(dash)
print(f"Upper Case Of Your Name is :  {upper_case}")
print(dash)
print(f"Lower Case Of Your Name is : {lower_case}")
print(dash)
print(f"Title Of Your Name is : {title}")
print(dash)



sentence ="  Hello, welcome to python programming language.  "

print(f"Original sentence is : {sentence}")

starting = sentence.startswith("Hello,")
ending = sentence.endswith("language")
couting = sentence.count("programming")
finding = sentence.find("welcome")
replacement = sentence.replace("python","Java")

print(dash)
print(f"Does the sentence start with 'Hello' : {starting}")
print(dash)         
print(f"Does the sentence end with 'language.' : {ending}")
print(dash)
print(f"Number of times 'programming' occurs in the sentence : {couting}")
print(dash)
print(f"Index of 'welcome' in the sentence : {finding}")
print(dash)
print(f"After replacing 'python' with 'Java' : {replacement}")
print(dash)
