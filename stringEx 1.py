# str1 = "Hello world"

# len
# print(len(str1))

# indexing
# print(str1[0]) #H
# print(str1[6]) #w
# print(str1[4]) #o

# print(str1[-2]) #l
# print(str1[-8]) #l

#substring [:]
# str1 = "Hello world"
# print(str1[:]) # [start:stop:step]
# print(str1[2:]) #
# print(str1[2:9])
# print(str1[:5])
# print(str1[::-1])

# s = 'hello'
# s1 = 'abc'
# print(s+s1)
# print(s+" "+s1)
# print(s1*5)

# str2 = "Hello world"
# print(str2.upper())
# print(str2.lower())
# print(str2.title())
# print(str2.capitalize())
# print(str2.swapcase())

# print(str2.count('o'))
# print(str2.count('l'))
# print(str2.find('o'))
# print(str2.find('o',5))
# print(str2.find('o',5,10))
# print(str2.find('o',8))

# print(str2.index('o'))
# print(str2.index('o',5))
# print(str2.index('o',5,10))
# print(str2.index('o',8))

# str3 = "         This is my string program       "
# print(str3.strip())
# print(str3.rstrip())
# print(str3.lstrip())

#f-string
# name = 'abc'
# age =21
# city= 'ahmedabad'

# my name is abc and I am 21 year old.I am leaving in ahmedabad.
# print(f'my name is {name} and I am {age} year old.I am leaving in {city}')


# format
# print("my name is {} and I am {} year old.I am leaving in {}".format(name,age,city))
# print("City:{2},Name:{0},Age:{1}".format(name,age,city))
# print("City:{city},Name:{name},Age:{age}".format(name='c',age=19,city='xyz'))

# a=10
# b=23.7
# c='a'
# print("a:%d","b:%f",'c%s:'%(a,b,c))

# str4 = "This is my string program"
# print(str4.split())
#
# str5 = "This is/my string/program"
# print(str5.split('/'))

str6 = ['This', 'is', 'my', 'string', 'program']
print(" ".join(str6))