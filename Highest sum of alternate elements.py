s = input().split(',')
lis = []
for i in range(len(s)):
    if(len(s)==1):
        lis.append(s[i][1:len(s[i])-1])
    elif(i==0):
        lis.append(s[i][1:])
    elif(i==len(s)-1):
        lis.append(s[i][0:len(s[i])-1])
    else:
        lis.append(s[i])
#print(lis)
s1 = 0
s2 = 0
for i in range(len(lis)):
    if i%2==0:
        s1+=(int(lis[i]))
    else:
        s2+=(int(lis[i]))
        
if(s1>s2):
    print(s1)
else:
    print(s2)
