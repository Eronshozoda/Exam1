c = int(input())
b = int(input()) 
cnt = 0
while c > 0:
    if c % 10 == b:
        cnt +=1
    c//= 10
print(cnt)