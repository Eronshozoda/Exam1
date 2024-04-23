n=int(input())
m=int(input())
s=0
while n<=m:
    if n%9==0:
      print (n)
    n+=1        
    s=s+n
print (s)    