## Lists


# ***


# list.sort() rearranges the elements of a list so that they are in order


print("\n***\n")



my_list = [3, 6, 4, 2, 1, 5]
my_list.sort()
print("sorts list of numbers ==> ", my_list)


print("\n***\n")



my_list2 = ['Cabbage', 'Apple', 'Banana', 'Potato']
my_list2.sort()
print("sorts list of words alphabetically ==> ", my_list2)


print("\n***\n")


my_list3 = ['This is a long sentence', 'Word', 'z']

my_list3.sort(key = len)
print("sorts list of words by length ==> ", my_list3)


print("\n***\n")



my_list4 = ['This is a long sentence', 'Word', 'z']
my_list4.sort(key = len, reverse=True)
print("sorts list of words by length reversed ==> ", my_list4)


print("\n***\n")



my_list5 = [('John', 2), ('Steve', 1), ('Joe', 3)]

def sort_tuple(tuple_value):

    return tuple_value[1]

my_list5.sort(key = sort_tuple)
print("sorts list of tuples by second key(the numbers) using a function passed in ==>", my_list5)


print("\n***\n")



# The sorted() function returns a sorted copy of the original list (nondestructive)


my_list6 = [3, 6, 4, 2, 1, 5]
sorted_list = sorted(my_list6)
print("original list ==> ", my_list6)
print("copy of list sorted ==> ", sorted_list)



print("\n***\n")


my_list7 = ["Bright", "Inquisitive", "Thoughtful"]
sorted_list2 = sorted(my_list7, key=len, reverse=True)
print("list sorted by length reversed ==> ", sorted_list2)




print("\n***\n")





list1 = [0, 1, 2, 3]
list1[0] = None
print("modifying list ==> ", list1)



print("\n***\n")




list2 = [0, 1, 2, 3]
list2.append(4)
print("appending element onto end of list ==> ", list2)


print("\n***\n")


## insert() ==> inserts element at any index, takes two arguments, index and value. if a value exists already at that index, new value is inserted before it and everything after is moved up by 1. if no value exists at the index, new value is added to the end of list


list3 = ["a", "b", "c", "d", "f"]
list3.insert(4, "e")
print("adding in 'e' at index[4] shifts f to index[5] ==> ", list3)


print("\n***\n")


list3.insert(1000, "g")
print("g is added to end of list because index[1000] does not exist ==> ", list3)












print("\n***\n")







print("\n***\n")










print("\n***\n")















print("\n***\n")















print("\n***\n")



print("\n***\n")















print("\n***\n")















print("\n***\n")















print("\n***\n")
