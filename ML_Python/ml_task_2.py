# Task 2 : Tower of Hanoi puzzle
from numpy import arange, ones

n=eval(input("Enter no. of disks: "))
position=ones(n, dtype=int)

def check(a):
    if(a==4):
        a=1
    if(a==0):
        a=3
    return a

def printer(a, check):
    mystr = " ".join(["Move disk",str(a),"from",str(position[a-1]),"->"])
    if((n+a)%2==0):
        position[a-1]-=1
    if((n+a)%2==1):
        position[a-1]+=1
    position[a-1]=check(position[a-1])
    mystr = " ".join([mystr,str(position[a-1])])
    print(mystr)

def move13(a):
    printer(a, check)
    for i in arange(1,a,1):
        move13(i)
        
for i in arange(1,n+1,1):
    move13(i)
