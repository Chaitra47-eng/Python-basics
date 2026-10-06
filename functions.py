#Built-in functions
# a,b,c = 100,3,400
# print(max(a,b,c))
# print(min(a,b,c))
# l1 = [1,4,6,3,-1]
# print(max(l1),min(l1))
# l1 = [1,4,6,3,]
# print(sum(l1))
# print(sum(l1,start=1))
# print(sum((a,b,c)))
# print(bin(10))
# print(oct(10))
# print(hex(10))

# #User defined function 
# def smith():
#     print("Singing")
# def Anu():
#     print("Dancing")
# print("start")
# smith()
# Anu()
# print("End")


#Types of user Defined Funcitons
#function without argument without return
# def add_two_numbers():
#     a=int(input('a:'))
#     b=int(input('b:'))
#     c=a+b
#     print(c)
# add_two_numbers()


#function without argument with return
# def add_two_numbers():
#     a=int(input('a:'))
#     b=int(input('b:'))
#     c=a+b
#     return c
# res = add_two_numbers()
# print(res)


#function with argument without return

# def add_two_numbers(a,b):
#     c=a+b
#     print(c)
# add_two_numbers(10,5)

#function with argument without return
# def add_two_numbers(a,b):
#     return a+b
# res = add_two_numbers(2,3)
# print(res)

#types of arguments
#positional argument
#Non default
# def fun(a,b):
#     print(a,b)
# fun(1,2)

# default 
# def fun(a,b=0):
#     print(a,b)
# fun(1,2)
# fun(1)
# fun(1,2,3)

# #keyword argument
# def fun(a,b,c):
#     print(a,b)
# fun(10,20,30)
# fun(a=10,b=20,c=30)
# fun(c=30,b=20,a=10)
# #fun(c=30,b=20,10)#SyntaxError: positional argument follows keyword argument
# fun(10,c=30,b=20)
# fun(10,c=30,a=100)#typeError

#arbitary variable argument
# def fun(*arg):
#     print(arg,type(arg)) 
# fun(1,2,3,4,5)
# fun()

# def fun(**arg):
#     print(arg,type(arg)) 
# fun(a=1,b=2,c=3)
# fun()
# fun(name="don",age=24)

# def fun(a,b=0,*arg1,**arg2):
#     print(a,b,arg1,arg2)
# fun(10,0,30,40,50,d=50,t=60)

#Nested function
# def function():
#     print("Hello i am fun")
#     def inner_fun():
#         print("Hi i am inner function")
#     inner_fun()
#     print("Bye Bye")
# print("Start")
# function()
# print("End")

#miscellenous Function
def fun():
    print("I am ironman")
r = fun
r()





