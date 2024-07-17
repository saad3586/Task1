'''Responsibility: Write a Python program to create a list, a
dictionary, and a set. Perform basic operations
like adding, removing, and modifying
elements.'''
# Create A List 
L = [1, 8, 7, 2, 21, 15 ]
# Add this value in list using append method
L.append(5)
# Revome this value in this using remove method
L.remove(1)
# Modifying
L[0]=10
print("Updating in Dictionary : ", L)


# Creating a Dictionary
d = {"name" : "saad",
     "from" : "India",
     "mark" : "92, 98, 96"}
# Adding
d["gender"] = "Male"

# Removing
d["from"]

# Modifying
d["mark"] = "77,56,34" 

print("Updating in Dictionary : ", d)

# Creating a Set
s = {1,2,3,5,6,7}

#adding
s.add(8)

# Removing 
s.remove(3)

# Modifying
s.discard(1)
s.add(12)

print("Updating in set: ", s)