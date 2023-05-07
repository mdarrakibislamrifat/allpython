countries=("Bangladesh","India","Pakistan","Japan","USA")
temp=list(countries)
temp.append("Russia")   #add item
temp.pop(3)             #remove item
temp[2]="Finland"       #change item
countries=tuple(temp)
print(countries)

countries1= ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries1 + countries2
print(southEastAsia)

tuple1=(1,3,4,5,7,8,9,0,3,5,2)
# res=tuple1.count(3)
# print("Count of 3 in tuples ",res)
# tuple1.index(4)
# print("Count of 3 in tuples ",res)
res=len(tuple1)
print(res)

