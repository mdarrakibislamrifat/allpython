# def average(a,b):
#     print("Average is",(a+b)/2)
# average(4,5)
def average(*numbers):
    print(type(numbers))
    sum=0
    for x in numbers:
        sum=sum+x
    print("Average is",sum/len(numbers))
average(5,5,5,5)