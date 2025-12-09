# def hello():
#     print("Hello! This function demo")
#
# hello()

# def addition(n1,n2):
#     n3 = n1+n2
#     print(n3)
#
# addition(10,5)

# def addition(n1,n2):
#     n3 = n1+n2
#     return n3
#
# add = addition(10,5)
# print(add)

# default
# def demo(n1,n2=90):
#     print("n1:",n1)
#     print("n2:",n2)
#
# demo(10,5)
# demo(10)

# keyword
# def demo(n1,n2):
#     print("n1:",n1)
#     print("n2:",n2)
#
# demo(10,5)
# demo(n2=10,n1=5)

# required
# def demo(n1,n2):
#     print("n1:",n1)
#     print("n2:",n2)
# try:
#     demo(10)
# except:
#     print("missing 1 required argument")

# variable-length
# def demo(*n1):
#     for i in n1:
#         print(i**2,end=" ")
#
# demo(1,2,3,4,5)

# def demo(*n1):
#     for i in n1:
#         print(i.upper(),end=" ")
#
# demo('AppLe','Banana','MaNgO')

# def demo(**n1):
#     for i,j in n1.items():
#         print(i,j)
#
# demo(a='abc',b='xyz')
