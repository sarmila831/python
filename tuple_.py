#tuple datatype and its functionalities
"""tup=(1,3,4,8,9,7)
print(type(tup), tup)
print(len(tup))
print(tup[1])
print(tup[-2])
print(tup[6-2])

tup2=tup[2:5]
print(tup2, "the tuple2 is")
thistuple = ("apple",)#for only one element in tuple we have to put coma after element
print(type(thistuple))
print(thistuple)
tup=(0,1,2,4,2,3,2,4,5,6,3,8,97,9,3,4,5,35,6,5)
res=tup.count(3)
print("Counting the occurance of 3 is : ",res)"""
#You can convert the tuple into a list, change the list, and convert the list back into a tuple.
'''thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
y.append("papaya")
thistuple = tuple(y)
print(thistuple)'''
#Adding tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)# created new tuple
thistuple += y #thistuple=thistuple + y

print(thistuple)