# #List

# names=["Mercy","Becca","Jebet","Miriam","Sheba","Vero","Abi","Methu"]
# first,second,third,*rest = names
# print(first)
# print(second)
# print(*rest)

# #sort
# numbers =[90,48,59,60,30,4,7,]
# numbers.sort()
# print(numbers)

# #reverse
# numbers.reverse()
# print(numbers)

# numbers.sort(reverse = True)
# print(numbers)


# #range only take intergers
# numbers = range(numbers[0])
# print(numbers)

# myList = [*range(10,20)]
# print(myList)

# # #del
# del(numbers[4])
# print(numbers)

# numbers.remove(30)
# print(numbers)

# number2 = set(numbers)
# print(number2)


# Dictionaries are made up of key-value pairs.Key is used to identify the item 
# and the value holds the value of the item.
# del is used to delete an element, variable and anything.
names1={'Yeke':1, 'bedi':2, 'Alex':3, 'Sheba':4}
del names1['Alex']

# dict.keys()
# Gets a minimum value from the dictionary
minimum ={'Ngano':150,'cereals':50,'Sweetcake':60 }
print(min(minimum,key=minimum.get))

# changing the value of a key in a nested dictionary
details={'Miriam':25,'Bridgo':253,'Becca':34}
details['Miriam']=23
print(details)

                # Tuples
# Lists are mutable while tuples are immutable
# indexing allows one to access a value
fruits=('orange','banana','mango','apple')
print(fruits[1])

# Copies a specific elements from one tuple to a new one
games=('Tennis','ball','draft','rugby')
fav=games[-2]
print(fav)

# Counts the number of occurrences
rivers=('Nairobi','Kigali','Yemen','Char','Zambezi')
print(rivers.count('Char'))

# lists
# reversing a list
numbs=[10,20,30,40,50]
numbs.reverse()
print(numbs)

# reversing a list in a descending order
numbers=[100,90,80,70,60]
numbers.sort(reverse=True)
print(numbers)

# range
myList=[*range(10,20)]
print(myList)

# alternative is using negative slicing

# Given list x = [1, 2, 3, 4, 5, 6, 7, 8, 9].
# Print the last element in the list
numx=[1,2,3,4,5,6,7,8,9]
numx.append(10)
print(numx)
numb=[90,80,70,60,50]
numb=numb[::-1]
print(numb)

# Removes empty strings from the list of strings
# Use filter()function to remove None type from the list
# remove None from list1 and convert result into list
names=('python','JavaScript','Kotlin')
name=list(filter(None,names))
print(name)

# sets
# Given the sets a = {1,2,3,4,5} and b = {4,5,6} print
# values in a but not in b
# Return a set of values that are in the first set but not in the second.
a={1,2,3,4,5}
b={4,5,6}
c=a.difference(b)
print(c)

# returning a set that contains values that are in both set
# return a set containing two values in two sets duplicates excluded.
d={1,2,3,4,5}
e={4,5,6}
f=d.union(e)
print(f)
# Returns a set containing value existing in both sets intersection