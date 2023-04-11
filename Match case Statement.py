x=int(input("Enter the value of x:"))
match x:
    case 0:
        print("It is zero")
    case 1:
        print("it is one")
    case 2:
        print("It is two")
    case 3:
        print("It is three")
    case _ if x!=90:
        print(x,"is not equal 90")
