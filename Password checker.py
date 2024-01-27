# Enter your code here. Read input from STDIN. Print output to STDOUT
string = input()
up = 0
low = 0
dig = 0
spe = 0
x = 0
rep = 0
if(len(string)>8):
    for i in string:
        if x!=0:
            if i==temp: rep+=1
        if i.isupper(): up+=1
        if i.islower(): low+=1
        if i.isdigit(): dig+=1
        if i in ["!","@","#","$","%","^","&","*","(",")","-","+"]: spe+=1
        x+=1
        temp = i
if(up>0 and low>0 and dig>0 and spe>0 and rep==0):
    print("True")
else:
    print("False")
