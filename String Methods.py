#strings are immutable

a="!! Rifat !!! Rifat"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Rifat","Rakib"))
print(a.replace("Rifat","Rohan"))
print(a.split(" "))

new="introduction To python"
print(new.capitalize())

str1="Welcome To my python world"
print(len(str1))
print(len(str1.center(50)))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Rifat. He is an honest man."
print(str1.find("is"))
# print(str1.index("ishh"))

str1="Rifat"
print(str1.isalnum())

str1="Welcome"
print(str1.isalpha)

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Healthy life\n"#here backslash n not printable string
print(str1.isprintable())

str1 = "     "       #using Spacebar
print(str1.isspace())

str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())