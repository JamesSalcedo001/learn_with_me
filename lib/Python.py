## Lists


# ***


# list.sort() rearranges the elements of a list so that they are in order

my_list = [3, 6, 4, 2, 1, 5]
my_list.sort()
print(my_list)

my_list2 = ['Cabbage', 'Apple', 'Banana', 'Potato']
my_list2.sort()
print(my_list2)


print("\n***\n")


my_list3 = ['This is a long sentence', 'Word', 'z']

my_list3.sort(key = len)
print(my_list3)

my_list4 = ['This is a long sentence', 'Word', 'z']
my_list4.sort(key = len, reverse=True)
print(my_list4)



my_list5 = [('John', 2), ('Steve', 1), ('Joe', 3)]

def sort_tuple(tuple_value):

    return tuple_value[1]

my_list5.sort(key = sort_tuple)
print(my_list5)


# The sorted() function returns a sorted copy of the original list


my_list6 = [3, 6, 4, 2, 1, 5]
sorted_list = sorted(my_list6)
print(my_list6)
print(sorted_list)
