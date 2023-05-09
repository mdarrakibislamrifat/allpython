X = "WELCOME TO MONEY GAMES\n\n\n"
quit1 = "'q' - for quit"
print(X.center(149))
questions = [
  ["What is the name of our Galaxy?", "Andromeda", "Milky way", "Orion", 'b'],
  [
    "What is the name of the theory that explains the origin of universe?",
    "Big Bang", "Black Hole", "Dark matter", 'a'
  ],
  [
    "What is the name of the largest planet of our Solar System?", "Saturn",
    "Neptune", "Jupiter", 'c'
  ],
  [
    "What is the name of the force that holds planets in orbit around the Sun?",
    "Electromagnetic force", "Gravitational force", "Strong force", 'b'
  ],
  [
    "What is the name of the brightest star in the night sky?", "Betelgeuse",
    "Sirius", "Polaris", 'b'
  ],
  [
    "How many comets are there in the Solar System?", "1 million", "1 billion",
    "1 trillion", 'c'
  ]
]
a2 = 1
level = 0
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000]
money = 0
for q in questions:
  x200 = f"Question is for ₹{levels[level]}\n"
  print(x200.center(150), quit1.center(150))
  print(f"{a2}.  {q[0]}\n\n"
        f"a. {q[1]}       b. {q[2]}       c. {q[3]}\n")
  input1 = input("Enter your answer: ")
  if input1 == q[4]:
    print(f"\n\nCorrect Answer!")
    print(f"You won ₹{levels[level]}")
    money = levels[a2 - 1] + money
    print(f"Total money you have is ₹{money}\n\n\n")
    a2 += 1
    level += 1
    continue
  if input1 == 'q':
    print(f"\n\nYou quit!\nTotal money taking for home is: {money}")
    break
  if input1 != q[4]:
    print("\n\nWrong Answer!\nTotal money taking for home is: 0")
    break
if a2 == 7:
  print(f"Congrats you did it\nTotal money taking for home is: {money}\n")
z = input("Press enter to exit")