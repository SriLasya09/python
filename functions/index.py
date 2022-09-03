ratings=[10,3,4,5,6,5.5,6.7]
#len
L=len(ratings)
print(L)
#sum
S=sum(ratings)
print(S)
#length of sum
L1=len([S])
print(L1)
#sorting
Sorted_list=sorted(ratings)
print(Sorted_list)
#using sort function
ratings.sort()
print(ratings)

#defining a function

#addition

def add1(a):
    b=a+1
    return b
c=add1(5)
print(c)

#multiplication

def Mult(a,b):
    c=a*b
    return c
d=Mult(6,3)
print(d)
e=Mult(2,'Lasya \n')
print(e)

def add1(a):
    b=a+1
    print(a,"plus 1 equals",b)
    return b
add1(2)

#enumerate

def printStuff(Stuff):
    for i,s in enumerate(Stuff):
        print("Album",i,"Rating is",s)
album_ratings=[10.0,8.5,9.5]
printStuff(album_ratings)
    
def ArtistNames(*names):
    for name in names:
        print(name)
ArtistNames("mJ","ac/dc","pink floyd")   


def AddDC(x):
    x=x+"DC"
    print(x)
    return(x)
x="AC"
z=AddDC(x)     

#global scope

def Thriller():
    Date=1982
    return Date
Date=2017
print(Thriller())
print(Date)

def ACDC(y):
    print(Rating)
    return(Rating+y)
Rating=9
Z=ACDC(1)
print(Rating)


def Pink():
    global sales
    sales='45 million'
    return sales
Pink()
print(sales)


