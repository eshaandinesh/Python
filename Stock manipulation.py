# Enter your code here. Read input from STDIN. Print output to STDOUT
#s = input().split(',')
i = "[1,2,8,4,5]"
s = i.split(',')
lis = []
for i in range(len(s)):
    if(len(s)==1):
        lis.append(int(s[i][1:len(s[i])-1]))
    elif(i==0):
        lis.append(int(s[i][1:]))
    elif(i==len(s)-1):
        lis.append(int(s[i][0:len(s[i])-1]))
    else:
        lis.append(int(s[i]))


n=1
while(n>0):
    if(len(lis)>1):
        if(lis[0]>lis[1]):
            lis.pop(0)
        elif(lis[len(lis)-2]>lis[len(lis)-1]):
            lis.pop()
        else:
            n-=1
    else:
        n-=1

print(lis)

share = 1
bp = 0
totals = [0]
prof = 0

for i in lis:
    if(share==1):
        bp = i
        print("Bought at ",bp)
        share = 0
        prof -= bp
        print("Profit ",prof)
    elif(share==0 and i>bp):
        share = 1
        print("Sold at ",i)
        prof+=i
        print("Profit ",prof)
        totals.append(prof)
                
print(totals)

print(max(totals))
