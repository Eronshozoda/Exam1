a=int(input())
cnt=0
i=1
while i<=a:
    if(a%i==0):
        cnt+=1
    i+=1
if cnt>2:
        print("The entered number is not a prime number.")
else:
    print("The entered number is a prime number.")