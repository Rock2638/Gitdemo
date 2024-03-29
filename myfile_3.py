#playing around with list

# set ariable as list
mylist = ["Jane", 57, "Christine", 53]
print(mylist)

#add an object at end of list
mylist.append("Joanne")
print(mylist)

#Returm position of Joanne in the list
print(mylist.index("Joanne"))

#Change an item in my list
mylist [1] =58
print(mylist)

#finding length of mylist
print(len(mylist))

#remove item from mylist
mylist.remove("Christine")
print(mylist)

#remove item given index
mylist.pop(0)
print(mylist)

mytuple = ("VBA", 100, True, "Carzy")
print(mytuple)