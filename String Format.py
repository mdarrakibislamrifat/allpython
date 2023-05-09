letter="Hey my name is {0} and i am from {1}"
country="Bangladesh"
name="Rifat"

print(letter.format(name,country))
print(f"Hey my name is {name} and i am from {country}")

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.32234324))


print(type(f"{2*30}"))
print(f"Hey my name is {{name}} and i am from {{country}}")