# select cursor up/down in selection
# Using shortcuts, made the elements into a list of dictionaries.
#Dictionaries

#this is a simple dictionary, with format [key]: [value], [key]:[value]
dictionary = {"name": "Fredrick", "number": 2}
#this is a list made from dictionaries.
list_o_dictionaries = [
    {"name": "Fredrick", "number": 2},
    {"name": "Todd", "number": 13},
    {"name": "Carlos", "number": 4}
]
#printing this will print the whole line of dictionary
print(dictionary)
#this will print the value of the key "name"
print(dictionary["name"])
sum = 0
#you can loop and enumerate through the list of dictionaries
for i, value in enumerate(list_o_dictionaries):
    print()
    #this will print the enumerated number
    print(i)
    #this will print the whole line of the dictionary
    print(value)
    #this will print the enumberated number and the value from the key "name"
    print(i,value["name"])

    # You can do math with the locations
    # another way to call a directiory  value.get("number")
    sum = sum + value["number"]
print(sum)    

#you can use enumerate on a dictionary
for i in enumerate (dictionary):
    #This will print the key, not the value
    print(i)
# or just loop through it normally
for i in dictionary:
    #this will print [key]: [value]
    print(f"{i}: {dictionary[i]}")