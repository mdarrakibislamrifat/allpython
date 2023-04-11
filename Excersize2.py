import time
timestamp=time.strftime('%H:%M:%S')
name=input("Enter you name:")
hour=int(input("Enter your hour:"))
if(hour>5 and hour<12):
    print("Hello Good morning",name)
elif(hour>=12 and hour<16):
    print("Hello good Afternoon",name)
elif(hour>=20 and hour<5):
    print("Hello good night",name)
else:
    print("Hello good evening",name)