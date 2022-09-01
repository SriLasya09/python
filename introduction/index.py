print("Hello")
print(25//6)
print(25/6)

#type conversion

print(type(22))
print(type(22.333))
print(str(1))
print(bool(1))
print(bool(0))
print(int(True))
print(int(False))

#operations

print(25+30*6)
print((25+30)*6)


#variables

my_variable=2
print(my_variable)
x = 160.0
y = 40
print(x+y)
print(type(x))
z=4
z=z/2
print(z)
total_min= 43+42+50
print(total_min)
total_hr = total_min/60
print(total_hr)

#strings 

Name = 'Lasya'
print(Name[1])
print(Name[-3])
print(Name[-2])
print(Name)
print("hello" + " " + Name)
print(len(Name))
print(Name[0:3])
print(Name[3:5])
print(Name[2:4])
print(Name[::2])
print(Name[0:5:2])
print(Name[0:3:2])
print(3 * "Name")
print(3 * Name )
print('I am the \n best')
print('I am the \t best')
print('I am the \\ best')
print(r'I am the \ best')


A = "well hi there"
B=A.upper()
print(B)
C=B.lower()
print(C)
D=A.replace('hi','hello')
print(D)

print(Name.find('ya'))
print(Name.find('ay'))

#lists & tuples

tuple1 = ('Lasya' , 10, 1.23)
print(type(tuple1))
print(tuple1[0])
print(tuple1[2])
print(type(tuple1[0]))
tuple2= tuple1 + ("hello", 10)
print(tuple2)
print(tuple1[1:3])
print(len(tuple2))
ratings= (10,9,3,5,7,2,4,8,1)
ratingsSorted= sorted(ratings)
print(ratingsSorted)

#nesting

nes= (1,2,("lasya","hello"),(3,4),("hi",(5,6)))
print(nes[2][1])
print(nes[2][1][3])
print(nes[3:5])
print((1,2,2)+ (2,3,4))

#lists

L=["lasya",10.1,2,3,4,5]
L.extend([30,50,"hi"])
print(L)
L1=[2,3,10.1,5,6,8]
L1.append([10.1,5,20,30])
print(L1)
L2=[1,2,3,4,5,7]
L2[1]=10
print(L2)
l3=[9,8,7,4,3,2,2]
del(l3[2])
print(l3)
l1=['hard rock']
l1="hard rock".split()
print(l1)
l2=["A,LAs,b,x,cv,b,gt,h,gf,n"]
l2="A,LAs,b,x,cv,b,gt,h,gf,n".split(",")
print(l2)
l4=[4,5,6,7]
l5=l4
print(l5[0])
l4[0]=9
print(l5)
l5[1]=100
print(l4)



#dictionaries

dict={"morning": 9 , "afternoon" : 2,  "evening":7}
print(dict["morning"])
dict['night']= 10
print(dict)
del(dict["morning"])
print(dict)
print(dict.keys())
print(dict.values())
print("night" in dict)
print("nig" in dict)


#sets

set2={"hi","hello","bye","hello"}
print(set2)

#type casting

list1=["hi",10, 1,"lasya",10,10]
set1=set(list1)
print(set1)
print(type(set1))
print(type(list1))
set1.add("hello")
print(set1)
set1.remove(1)
print(set1)
print(10 in set1)
set2={"lasya",10,10,5,6}
set3=set1&set2
print(set3)
print(set1.union(set2))
print(set3.issubset(set1))