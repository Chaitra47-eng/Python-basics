# Check if a number is even or odd
#val = int(input("Enter a number: "))
#if val % 2 == 0:
# # print(f"{val} is even.")
# #else:
# # print(f"{val} is odd.")


# #print("Hello, World!")

# a = input("select an operation:add, sub, mul, div: \n option: ")
# val1 = int(input("Enter first number: "))
# val2 = int(input("Enter second number: "))
# match a:
#     case "add":
#       res = val1 + val2
#       print("result = ", res)

#     case "sub":
#       res = val1 - val2
#       print("result = ", res)

#     case "mul":
#       res = val1 * val2
#       print("result = ", res)

#     case "div":
#       res = val1 / val2
#       print("result = ", res)
    
#     case _:
# #          print("Invalid operation selected.")  

# n=int(input("Enter a number: "))
# match n:
#       case 1|5|7:
#          print("iron man")
#       case 2:
#          print("bat man")
#       case 3:
#          print("DON")
#       case _:
#          print("SHakti man")   

# n=int(input("Enter a number: "))
# match n%2:
#     case 0:
#         print("Even")
#     case 1:
#         print("Odd")


# for i in range(1,11,1):
#     print("i")

# for val in range(1,11,1):
#     print(val, end=' ')

# for val in range(1,10):
#     print(val, end=' ')

# for val in range(10):
# #     print(val, end=' ')

# for val in range(1,11,2):
#     print(val, end=' ')
# for val in range(2,100,2):
#     print(val, end=' ')


# for val in range(10,0,-1):
#     print(val, end=' ')

# n=int(input("n: "))
# for i in range(1,n+1):
#     if i%2==0:
#       print(i, end=' ')

# n=int(input("n: "))
# for i in range(1,n+1):
#     print(i**2, end=' ')

# n=int(input("n: "))
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")
#     n=int(input("n: "))


# n=int(input("n: "))
# for i in range(1,n+1):  
#      if i%2!=0:
#         print(i, end=' ')

# s1="pyspider"
# for i in s1:
#     print(i, end=' ')

# names = ["John", "Alice", "Bob", "Eve"]
# for name in names:
#     print(name,end=' ')

# i= 1
# while i<11:
#     print(i, end=' ')
#     i+=1
# i=10
# while i>0:
#     print(i, end=' ')
#     i-=1

# for i in range(1,4):
# #    for j in range(1,5):
# #        print(i,end=' ')

# i=1
# while i<=3:
#     j=1
#     while j<=4:
#         print(i,end=' ')
#         j+=1
#     i+=1

# for i in range(1,10):
#    if i==4:
#       break
#    print(i,end=' ')

# x=0
# for i in range(3):
#    for j in range(i):
#       x+=1
# else:
#    x+=5
#    print(x)

# x=0
# while x<3:
#     print(x,end=" ")
#     x+=1
# else:
#     print("done")

# for i in range(2):
#     for j in range(2):
#         if i==1 and j==1:
#             break
#     print(i,j)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b:
#     if a >= c:
#         largest = a
#     else:
#         largest = c
# else:
#     if b >= c:
#         largest = b
#     else:
#         largest = c

# print("Largest number is:", largest)

# for i in range(1,51):
#     if i%2==0:
#         print(i, end=' ')

# n=int(input("n: "))
# if n%3==0 and n%5==0:
#     print(f"{n} is divisible by both 3 and 5.")
# else: 
#     print(f"{n} is not divisible by both 3 and 5.")   

# i=10
# while i>0:
#     print(i, end=' ')
#     i-=1

# ...existing code...

# n = int(input("Enter n: "))

# # Using for loop
# sum_for = 0
# for i in range(1, n + 1):
#     sum_for += i
# print("Sum using for loop:", sum_for)

# # Using while loop
# sum_while = 0
# i = 1
# while i <= n:
#     sum_while += i
#     i += 1
# # print("Sum using while loop:", sum_while)


# l1=[10,20,30,40,50,60,70,80]
# print(l1)
# print(l1[1:4:1])
# print(l1[2:7:1])
# print(l1[1:4])
# print(l1[:4])
# print(l1[1:100])
# print(l1[: :])
# # print(l1[1:4:0])
# print(l1[5:1:-1])
# print(l1[: : 2])
# print(l1[: : -1])
# print(l1[: : -2])
# print(l1[-1:4:-1])
# print(l1[1:6:-1])
# print(l1[6:1:1])

l1=[10,20,30,40,50,60,70,80]
# for i in l1:
#     print(i, end=' ')

# print()
# for i in range(len(l1)):
#     print(l1[i], end=' ')

# i=len(l1)-1
# while i>=0:
#     print(l1[i], end=' ')
#     i-=1

# print(l1)
# # list.clear(l1)
# # print(l1)

# l1=[i for i in range(1,101)]
# print(l1)
# l1=[i for i in range(1,101) if i%2==0]
# print(l1)
# n=int(input("n: "))
# l1=[i for i in range(1,n+1) ]
# print(l1)
# n=int(input("n: "))
# l1=[100 for i in range(1,n+1) ]
# print(l1)
# n=int(input("n: "))
# l1=[[1,2,3]for i in range(1,n+1) ]
# print(l1)

# l1=[10,20,30]
# l2=[40,50,60]
# print(l1+l2)

# l3=[4,5,6]
# print(l3*3)
t1=(10,20,30,40,50)
# print(t1)
# print(type(t1))
# print(len(t1))
#t1.append(60)  # This will raise an AttributeError because tuples are immutable
# print(t1*3)
# t2=(1,2,3)
# print(t1+t2)
# for i in t1:
#     print(i, end=' ')

# s1={10,20,30,6.5,True,3+6j,'py', 10}
# s1.add(50)
# s1.update([23,45,67])
# s1.remove(30)
# print(s1)
# print(type(s1))
# print(len(s1))
s1={10,20,30,40}
# print(s1)
# s1.add(50)
# print(s1)
# s1.update((60,70,80))
# s1.remove(50)
# s1.discard(40)
# s1.pop()
# s2=s1.copy()
# s1.clear()

# print(s1)

# d={1:2,"a":"apple","aa":"apple","a":"animal"}
# print(d,type(d),len(d))
# print(d["a"])
# d["aa"]="ant"
# d.update({4:5,"b":"bat","c":"cat"})
# d.update(b="bat",d="doll")
# d.update([("h","horse"),("e","Elephant")])
# d1=d.copy()
# d.clear()
# res=d.setdefault(1)
# res1=d.setdefault(3)
# res2=d.setdefault(3,"three")
# # print(res2,d)
# <-- Dict pop-->

# res=d.pop(1)
# print(res,d)
# res1=d.pop(3)
# print(res1,d)
# res2=d.pop(3,'three')
# print(res2,d)
#  <--Dict get()-->
# res=d.get(1)
# print(res,d)
# res1=d.get(3)
# print(res1,d)
# res2=d.get(3,"three")
# print(res2,d)
d={1:2,"a":"apple",4:16}
# res=d.popitem()
# print(res,d)
# res1=d.popitem()
# print(res1,d)
# res2=d.popitem()
# print(res2,d)

# d={}
# l=[1,"a",2,"b",3]
# res_d=d.fromkeys(l)
# print(res_d)
# res_d1=d.fromkeys([1,2,3],"py")
# print(res_d1)
# res_d2=d.fromkeys("RAT","py")
# print(res_d2)

# res_k=d.keys()
# print(res_k)
# d.update({"b":"bat"})
# print(res_k)

# res_v=d.values()
# print(res_v)
# d["a"] = "ant"
# print(res_v)

# res_i =d.items()
# print(res_i)
# d.popitem()
# print(res_i)

# d={i:i for i in range(1,101)  if i % 2==0}
# print(d)
# s={i:i**3 for i in range(1,50)}
# s={i:i for i in range(1,71) if i%7==0}
# # s={i:i for i in range(1,11) if i%2!=0}
# s={n:n for n in range(1,11) if F(n)=F(n-1)+F(n-2)}
# print(s)
# s = "PYspider@123"
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# s = "MY name IS ChaITra" 
# print(s.title())
# print(s.casefold())
# print(s.swapcase())

# s1="pyspiders"
# print(s1.partition("s"))
# print(s1.partition("l"))
# print(s1.rpartition("l"))
# print(s1.partition("sp"))
# print(s1.partition("i"))
# print(s1.rpartition("i"))
# print(s1.partition("s"))
# print(s1.rpartition("s"))

# # l=["python","is","very","Easy"]
# # s="Hello"
# # res="".join(l)
# # print(res)
# # res1="_".join(s)
# # print(res1)

# s="python is easy,python is simple"
# print(s)
# print(s.replace(" ","_"))
# print(s.replace(" ","_",2))
# print(s.replace(" ","_",9))
# print()
# s1= "H E L L O"
# print(s1.replace("E","e"))
# print(s1.replace("O","0"))
# print(s1.replace("K","e"))
# print(s1.replace("L","l"))
# print(s1.replace("E","EE"))
# print(s1.replace("LL","l"))
# print()
# s2 = "pyspiders"
# print(s2.replace("py","Q"))
# print(s2.replace("ers","ERS"))
# print(s2.replace("psies","PSIES"))

# num=4
# res = str(num)
# print(len(res),type(res))
# print(res.zfill(0))
# print(res.zfill(1))
# print(res.zfill(2))
# print(res.zfill(6))
# print(res.zfill(-2))
# print()
# print("-3".zfill(3))
# print("+3".zfill(3))
# print("*3".zfill(3))

s= "good"
# print(len(s))
# print(s.center(6))
# print(s.center(6,"~"))
# print(s.center(9,'*'))
# print(s.center(9,'*~'))

# s1 = "bad"
# print(len(s1))
# print(s1.center(5))
# print(s1.center(5,"_"))
# print(s1.center(8,'*'))
# s2 = "python"
# print(s2.ljust(10,"^"))
# print(s2.rjust(10,"^"))

# strip
# s="  python            "
# print(s,len(s))
# res = s.strip()
# print(res,len(s))
# print("..#..py.#.".strip('.'))
# print("..#..py.#.".strip('.#'))
# print("..#..py.#.".strip('.#p'))
# print("..#..py.#.".strip('None'))
# print("  py  ".strip(None))

# s = "  python         "
# print(s,len(s))
# res = s.lstrip()
# print(res,len(res))
# res1 = s.rstrip()
# print(res1,len(res1))
# print("..#..py..#..#".lstrip('y'))
# print("..#..py..#..#".rstrip('.'))
# print("..#..py..#..#".lstrip('.#'))
# print("..#..py..#..#".rstrip('.#'))
# print("..#..py..#..#".lstrip('.#p'))
# print("..#..py..#..#".rstrip('.#p'))
# print("..#..py..#..#".lstrip(None))
# # print("..#..py..#..#".rstrip(None))


# s = "  python         "
# print(s,len(s))
# res = s.lstrip()
# print(res,len(res))
# res1 = s.removeprefix(" ")
# print(res1,len(res1))
# print(s.removeprefix(" "))
# print(s.removeprefix("  "))
# print(s.removeprefix("    "))
# print("..#..py..#..#".lstrip('.#p'))
# print("..#..py..#..#".removeprefix('..#..p'))
# print("..#..py..#..#".removeprefix('.#p'))

# s= "p\ty"
# print(s)
# s1="H\tE\tLL\to"
# print(s1)
# print(s1.expandtabs())
# print(s1.expandtabs(4))
# print(s1.expandtabs(10),len(s1))
# print(s1.expandtabs(0))
# print(s1.expandtabs(-4))

# s = "  python         "
# print(s,len(s))
# res = s.lstrip()
# print(res,len(res))
# res1 = s.removesuffix(" ")
# print(res1,len(res1))
# print(s.removesuffix(" "))
# print(s.removesuffix("  "))
# print(s.removesuffix("    "))
# print("..#..py..#..#".lstrip('.#p'))
# print("..#..py..#..#".removesuffix('..#..p'))
# print("..#..py..#..#".removesuffix('.#p'))

# s="The person name is {} and age is {} and from the place {}"
# print(s.format("king",45,"Mysore"))
# s1 = "The person name is {name} and age is {age} and from the place {place} "
# print(s1.format(name='Queen',age=34,place="Bangalore"))

# s2 = "{name1} and {name2} are good friends"
# map_obj = {'name1':'Jack','name2':'Jill'}
# print(s2.format_map(map_obj))

# s = "Hello"
# res = s.encode()
# print(res)


# s="Beautifull"
# print(s.startswith("B"))
# print(s.startswith("b"))
# print(s.startswith("Bea"))
# print(s.startswith("Beu"))
# print(s.startswith("a"))
# print(s.startswith("a",2))
# print(s.startswith("au",2,5))
# print(s.startswith("au",2,3))
# # print(s.startswith("B","k","p","l"))
# # print(s.startswith("b","k","p","l"))
# print(s.startswith("a","l"),2)

# print(s.endswith("l"))
# print(s.endswith("L"))
# print(s.endswith("ll"))
# print(s.endswith("le"))
# print(s.endswith("FULL"))
# print(s.endswith("f",2))
# print(s.endswith("fu",6,8))
# print(s.endswith("au",2,6))
# # print(s.endswith("B","k,"l","p"))
# print(s.endswith("l"))
# print(s.endswith("l"))

# print("PYTHON".isupper())
# print("PYTHOn".isupper())
# print("PYTHON@123".isupper())
# print("PYTHOn2123".isupper())


# print("hello".islower())
# print("Hello".islower())
# print("hello@123".islower())
# print("hellO@123".islower())

# print("Rose are good".istitle())
# print("Rose Are Good".istitle())
# print("Rose Are GooD".istitle())
# print("Ro$e are good".istitle())
# print("Ro$Es are good".istitle())

# print("py".isalpha())
# print("py12@".isalpha())


# print("py123".isalnum())
# print("py@123".isalnum())
# print("py".isalnum())
# print("123".isalnum())

# print("a2".isidentifier())
# print("2a".isidentifier())
# print("a_b".isidentifier())
# print("a*b".isidentifier())
# print("_".isidentifier())
# print("if".isidentifier())
# print("while".isidentifier())

# print("".isspace())
# print(" ".isspace())
# print("a  b".isspace())
# print("a\nb ".isspace())
# print("\n ".isspace())
# print(" \t".isspace())

# print("py@123".isprintable())
# print("\n".isprintable())
# print("\t".isprintable())

# print("py@123".isascii())
# print("😊".isascii())
# print("Â".isascii())
# print(" ".isascii())
# print("₹".isascii())

# print("5³".isnumeric())
# print("4".isnumeric())
# print("⅓".isnumeric())
# print("ⅴ".isnumeric())
# print("八".isnumeric())
# print("123".isnumeric())

print("5³".isdigit())
print("4".isdigit())
print("⅓".isdigit())
print("ⅴ".isdigit())
print("八".isdigit())
print("123".isdigit())

print("5³".isdecimal())
print("4".isdecimal())
print("⅓".isdecimal())
print("ⅴ".isdecimal())
print("八".isdecimal())
print("123".isdecimal())














