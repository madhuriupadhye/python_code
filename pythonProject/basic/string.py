print("Hello World!")
new_dessert = "fig pie"
print(new_dessert[0:3])
print(new_dessert[-1])
print(new_dessert[::-4])
word = "boil"
word = "f" + word[1:] # replace of string, as strings are immutable
word1 = "f" + word[2:]
print(word) # foil
print(word1) # fil
print(len(word))
print(word.upper())
print(word.lower())
startship = "Enterprise"
print(startship.startswith("N")) # return True or False
day = "Thursday"
egg = 3
becon = 3
print(f"{day}'s breafast is {egg} eggs and {becon} beccons")
