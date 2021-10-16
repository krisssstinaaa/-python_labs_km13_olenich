
phrase1 = input("Please, enter the first phrase: ")
phrase2 = input("Please, enter the second phrase: ")
phrase1 = "".join(c for c in phrase1 if c.isalpha())
phrase2 = "".join(c for c in phrase1 if c.isalpha())
set1 = {i.lower() for i in phrase1}
set2 = {i.lower() for i in phrase2}
if set2.issubset(set1) == True:
    print("The first phrase can turn into the second!")
else:
    print("The first phrase can not turn into the second!")