import vor
"""
a = "1235" ################# int
b = "12.4" ################# float
c = "ali"  ################# str_fh 
d = "ali0098" ############## str_g 
e = ""     ################# khali

f = 1234
g = 123.4
h = ["1","a"]
i = False
j = None
k = (1,2)

print(vor.chek(a))
print(vor.chek(b))
print(vor.chek(c))
print(vor.chek(d))
print(vor.chek(e))

print("\n\n\n")

print(vor.chek(a , "int" ))
print(vor.chek(b , "float" ))
print(vor.chek(c , "str_fh" ))
print(vor.chek(d , "str_g" ))
print(vor.chek(e , "khali" ))

print("\n\n\n")

print(vor.chek(f))
print(vor.chek(g))
print(vor.chek(h))
print(vor.chek(i))
print(vor.chek(j))
print(vor.chek(k))

print("\n\n\n")

print(vor.chek(f , "int" ))
print(vor.chek(g , "float" ))
print(vor.chek(h , "list" ))
print(vor.chek(i , "bool" ))
print(vor.chek(j , "none" ))
print(vor.chek(k , "tuple"))
"""


# Example

val = input("Enter : ")

if vor.chek(val) == "int" :
    print ("The value entered by the user is an integer")
    val = int(val)
elif vor.chek(val) == "float" :
    print ("The value entered by the user is an float")
    val = float(val)
elif vor.chek(val) == "str_fh" :
    print ("The value entered by the user is only letters")
elif vor.chek(val) == "str_g" :
    print ("The value entered by the user is mixed")
elif vor.chek(val) == "khali" :
    print ("The value entered by the user is empty")