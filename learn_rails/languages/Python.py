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

## del() removes elements from a list specified by an index or range of indices, destructive

list4 = ["a", "b", "c", "d", "e", "f", "g"]
del(list4[0])
print("deleting index[0] ==> ", list4)

print("\n***\n")



del(list4[0:3])
print("deleting from index[0] to index[3] ==> ", list4)



print("\n***\n")



## pop() removes and returns element at index passed in as argument. when used without arguments, removes and returns last element, destructive


list5 = ["a", "b", "c", "d", "e", "f", "g"]

print("returns element removed ==> ", list5.pop())


print("\n***\n")

print("popping off element at index[0] and returning it ==> ", list5.pop(0))

print("\n***\n")



## remove() removes element passed in as argument, one of few list methods that searches by value INSTEAD of index, destructive


list5.remove("f")
print("using remove() to find and delete 'f' element, does not return element after removing ==> ", list5)




print("\n***\n")


## clear() erases all values of list, fast way to free up memory on device if working with large list in Python shell


list5.clear()
print("deletes entire list ==> ", list5)



print("\n***\n")

## range(start_val, end_val, step_size) => simple type of sequence commonly used in for loops, only contain integers in fixed pattern, build a range using range() constructor method and loop through it as it were a standard list. minimum one argument: end of range. one can add two more optional arguments, start value and step size,

for n in range(4):
    print("printing range(4) ==> ", n)

print("\n***\n")

for n in range(1, 4):
    print("printing range(1, 4) ==> ", n)

print("\n***\n")

for n in range(0, 4, 2):
    print("printing range(0, 4, 2) ==> ", n)

print("\n***\n")


## each iteration is printed out










print("\n***\n")















print("\n***\n")



print("\n***\n")















print("\n***\n")















print("\n***\n")















print("\n***\n")




















## String Methods: all return new object, nondestructive




# 1: for..in loop / indexing strings, they are iterable and are indexed


string_1 = "Hello World!"
for char in string_1:
    print("showing each iteration of the string ==> ", char)

print("\n***\n")


print("accessing index of 'Hello World!' => ", string_1[0])
print("accessing index of 'Hello World!' => ", string_1[1])
print("accessing index of 'Hello World!' => ", string_1[3])



print("\n***\n")



# 2: upper() returns an uppercase version of the original string, lower() returns a lowercase version, and title() returns the original string with the first letter of each word capitalized

string_2 = "Hello world!"

print(string_2.upper())
print("\n***\n")

print(string_2.lower())
print("\n***\n")

print(string_2.title())
print("\n***\n")











print("\n***\n")
