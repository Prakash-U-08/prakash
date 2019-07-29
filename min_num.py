from itertools import combinations
n,k=list(map(int,input().split()))
n=list(str(n))
no_of_combinations=len(n)-k
a=list(combinations(n,no_of_combinations))
min_num=min(a)
m="".join(min_num)
m=int(m)
print(m)
