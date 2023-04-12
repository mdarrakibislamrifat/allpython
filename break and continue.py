# for x in range(11):
#     if(x==6):
#         print("Loop out")
#         continue
#     print("5 x",x+1,"=",5*(x+1))
    
# # print("Loop out")

i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break


while True:
      number = int(input("Enter a positive number: "))
      print(number)
      if not number > 0:
       break