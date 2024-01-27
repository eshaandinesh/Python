# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
lis = []
row = []
for i in s:
    if i.isdigit():
        row.append(int(i))
    if i==']' and len(row)>0:
        lis.append(row)
        row = []

r = len(lis)
c = len(lis[0])

row = []
gen = []
sum = 0
for m in range(r):
    for n in range(c):
        try: 
            sum+=lis[m-1 if m>0 else r][n-1 if n>0 else c]
        except IndexError:
            sum+=0
        try: 
            sum+=lis[m-1 if m>0 else r][n]
        except IndexError:
            sum+=0
        try: 
            sum+=lis[m-1 if m>0 else r][n+1]
        except IndexError:
            sum+=0
        try: 
            sum+=lis[m][n-1 if n>0 else c]
        except IndexError:
            sum+=0
        try: 
            sum+=lis[m][n+1]
        except IndexError:
            sum+=0
        try: 
            sum+=lis[m+1][n-1 if n>0 else c]
        except IndexError:
            sum+=0
        try: 
            sum+=lis[m+1][n]
        except IndexError:
            sum+=0
        try: 
            sum+=lis[m+1][n+1]
        except IndexError:
            sum+=0
    
        if(lis[m][n]==0):
            if(sum==3):
                row.append(1)
            else:
                row.append(0)
        if(lis[m][n]==1):
            if(sum<2):
                row.append(0)
            elif(sum>3):
                row.append(0)
            else:
                row.append(1)
            
        sum = 0
    gen.append(row)
    row = []
print(gen)
