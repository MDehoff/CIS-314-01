import random

tuples = ("PWedge", "9Iron","8Iron","7Iron","6Iron","5Iron","4Iron","5Wood","3Wood","Driver")
lists = ("Driver","3Wood","5Wood","4Iron","5Iron","6Iron","7Iron","8Iron","9Iron","PWegde")

print(tuples)
print(lists)

randomtup = random.sample(tuples, len(tuples))
print("This is the random tuples: ",randomtup)

randomlis = random.sample(lists,len(lists))
print("This is the random lists: ",randomlis)

newtuple = list(tuples)
newtuple.append("3Iron")
tuples = tuple(newtuple)
print("Tuple with the 11th element: ",tuples)

newlist = list(lists)
newlist.append("3Iron")
lists = tuple(newlist)
print("List with the 11th element: ",lists)

print("Tuple with the first element removed: ",tuples[1:])
print("List with the first element removed: ",lists[1:])

newtuple = list(tuples)
newtuple.pop(1)
tuples = tuple(newtuple)
print("Tuple with the '9Iron' removed: ",tuples)

newlist = list(lists)
newlist.pop(8)
lists = tuple(newlist)
print("List with the '9Iron' removed: ",lists)
