'''              Lists 
1) Lists are like arrays except that they can be heterogeneous
2) Lists are mutable (append,insert,updating by indexing)   
3) Lists are ordered and have a definite index  
4) They allow duplicate values '''

list1=["tanya","sinha",34,89]
print(list1)

list1[2]=67
print(list1)
list1.append("aman")
print(list1)
list1.insert(3,"raj")
print(list1)
# Addition of multiple elements to the List at the end 
list1.extend([8, 'Geeks', 'Always']) 
print(list1)

print(list1[0])
print(list1[1:3])

list1.remove(89)
print(list1)
print(len(list1))

list2=["tanya","tanya"]
print(list2)


''' Tuples
1) Tuples are like lists , i.e they are heterogeneous
2) Unlike Lists , Tuples are immutable
3) Tuple elements are also accessed by index  '''

tuple1=("tanya","sinha",34,89)
print(tuple1)

# No insert , append on tuple as they are immuatble
# to chnage tuple convert to list
list2=list(tuple1)
print(list2)

print(tuple1[0:3])

# Elements cannot be removed one by one as they are immuatble
# we have entire delete a tuple
del tuple1



'''     Dictionary
Values can be duplicated but keys must be unique '''

dict1={"tanya":22,"sinha":25,"aman":13,"raj":15}
print(dict1)

print(dict1.keys())
print(dict1.values())
#items()	Returns a list of dict’s (key, value) tuple pairs
print(dict1.items())

#accessing an value is done by key
print(dict1["tanya"])



''' Sets
1) They are mutable
2) They are unordered so no accessing by index
3) No duplicate values are allowed   '''

set1=set(["tanya","sinha",34,89])
print(set1)

set1.add(78)
print(set1)

# sets are unordered cannot access by index so we use loop
for i in set1:
    print(i,end=" ")

















