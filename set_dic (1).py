# set :- {},mutable,unorder
# s1 = set()
# print(type(s1))
#
# # add,update
# s1.add(10)
# s1.add('a')
# s1.add('b')
# print(s1)
#
# s1.update(['c','d',95.3,34])
# print(s1)
#
# # remove,discard,pop,clear
# s1.remove('c')
# print(s1)
#
# s1.discard(34)
# print(s1)
#
# s1.pop()
# print(s1)
#
# s1.clear()
# print(s1)

#union
# s2 ={1,2,3,4,5,6,7}
# s3 ={2,5,6,8,9,10,11}
# print(s2|s3)
# print(s2.union(s3))

# intersection
# print(s2&s3)
# print(s2.intersection(s3))

# difference
# print(s2-s3)
# print(s3.difference(s2))

# symmetric difference
# print(s2^s3)
# print(s2.symmetric_difference(s3))

# dictionary:-{},key:value,key always unique
d={1:'a',2:'b'}
d[3]='c'
d[4]='d'
d[5]='e'
print(d)
d[5]='h'
print(d)

d1={6:'x',7:'y'}
d.update(d1)
print(d)

# default keys
# for i in d:
#     print(i)

# for i in d.values():
#     print(i)

# for i in d.items():
#     print(i)

# for i,j in d.items():
#     print(i,"->",j)

# print(d[2])

# for i in d:
#     print(i,'->',d[i])

# pop,popitem
# d.pop(4)
# print(d)
# 
# d.popitem()
# print(d)
#
# del d[3]
# print(d)
#
# d.clear()
# print(d)