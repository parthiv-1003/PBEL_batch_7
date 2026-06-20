#List
my_list = [1,2,3,4,5]
print(my_list)
print(type(my_list))

#properties and method
print(len(my_list))
my_list.append(6) #is used to add element to the end 
print(my_list)
my_list.insert(0,0) # is uesd to add in a specific position
print(my_list)

my_list.extend([7,8,9]) 
print(my_list)

my_list.remove(3)
print(my_list)

my_list.pop()
print(my_list)


#properties
print(my_list[7])

#ordered  and mutable
my_list[7] = 10
print(my_list)

#duplicacy and heterogeneity
FUN = [1,2,3,4,12,1,2,True, False,"Hello"]
print(FUN)

#Tuple
abc = (1,2,3,4,5)
print(abc)
print(type(abc))


#set 
my_set = {1,2,3,4,5}

#dictionaries
