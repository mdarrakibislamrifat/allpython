a=int(input("Enter you age:"))
print("Your age is ",a)
# conditional operators
# >,<,>=,<=,==,!=
# print(a>18)
# print(a>=18)
# print(a==18)
# print(a!=18)
if(a>18):
    print("You can drive")
else:
    print("You can not drive")
print("Hi i am Rifat")

applePrice=int(input("Enter apple price:"))
budget=int(input("Enter your budget:"))
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")

num=int(input("Enter a number:"))
if(num>0):
    print("It is a positive number")
elif(num==0):
    print("It is zero")
elif(num==999):
    print("It is a special number")
else:
    print("It is negative")
print("I ma happy now")

#Nested if else
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

 

