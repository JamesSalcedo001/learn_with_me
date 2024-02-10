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
