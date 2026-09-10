mark=eval(input("Enter list of mark"))
def hz(mark):
    d={}
    s=""
    for i in mark:
        s+=str(i)
    for i in mark:
        if i not in d:
            
            d[i]=s.count(str(i))
    return d 
def stats(mark):
    print(f"maximum mark is :{max(mark)}")
    print(f"mininmum mark is :{min(mark)}")
    print(f"total mark is:{sum(mark)}")
    print(f"average mark is {sum(mark)/len(mark)}")
    c=0
    l=[]
    for i in mark:
        if i not in l:
            c+=1
            l.append(i)
        
    print(f"no: of distinct mark is :{c}")
def higest():
    dmark=hz(mark)
    c=[]
    for i in dmark:
        if dmark[i]>c:
            c.append(dmark[i])
            c.append(" the frquency of given mark is "+str(i)+"\n")
        if c==dmark:
            c.append(dmark[i])
            
            c.append(" the frquency of given mark is "+str(i)+"\n")
for i in c:
    print(i,end="")
    
 higest()       