
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
    dmark = hz(mark)
    highest = max(dmark.values())

    for i in dmark:
        if dmark[i] == highest:
            print("The frequency of", i, "is", highest)

def search(mark):
    smark=int(input("enter a mark:"))
    if smark in mark:
        print("The mark exist!")
        n=hz(mark)
        print(n[smark])
while True:
    print("1.frequency dictionary")
    print("2.stats")
    print("3.analysis")
    print("4.search")
    print("5.exit")
    print()
    choice=int(input("Enter a choice(1,2,3,4,5): "))
    print()
    mark=eval(input("Enter list of mark"))
    if choice==1:
        hz(mark)
    elif choice==2:
        stats(mark)
    elif choice==3:
        higest(mark)
    elif choice==4:
        search()
    elif choice==5:
        print("bye!!")
        break
    else:
        print("invalid chice")
        print()