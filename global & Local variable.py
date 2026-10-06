# a = 100
# def fun():
#     b = 200
#     print("Inside fun:",a)
#     print("Inside fun:",b)
# fun()
# print("outside fun:",a)
# print("outside fun:",b)
# fun()

# a=100
# def fun():
#     b=200
#     def inner_fun():
#         c=300
#         print(c,b,a)
#     inner_fun()
# fun()

# a=100
# def fun():
#     a=200
#     print(a)
# fun()

# a=100
# def fun():
#     a=200
#     print(a,id(a))
# print(a,id(a))
# fun()
# print(a,id(a))

# a=100
# def fun():
#     b=200
#     print(b)
#     def inner_fun():
#         nonlocal b
#         b=300
#         print(b)
#     inner_fun()
#     print(b)
# fun()

a=100
def fun():
    global a
    a=200
    print(a,id(a))
print(a,id(a))
fun()
print(a,id(a))