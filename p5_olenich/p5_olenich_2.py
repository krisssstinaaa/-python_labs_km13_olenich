#This program is used for outpitting information from user.
mylist = []
mylist = input("Enter elements of the list: ").split()
#"If" is used to consider 2 cases: when number of elements is 1 and whem it is bigger than 1.
if len(mylist) > 1:
    print(", ".join(mylist[:-1]), "and", mylist[-1])
if len(mylist) <= 1:
    print(*mylist)
