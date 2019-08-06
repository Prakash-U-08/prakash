def gcd(x,y):
    while(y):
        x,y=y,x%y
    return x
n,q=input().split()
n=int(n)
q=int(q)
list1=[]
a=list(map(int,input().split(" ",n-1)))
for i in range(q):
    l=input().split()
    if(len(l)>1):
        l[0]=int(l[0])
        l[1]=int(l[1])
        g=gcd(l[0],l[1])
        list1.append(g)
    else:
        list1.append(l[0])
for i in list1:
    print(i)
    
    
    
    
    


