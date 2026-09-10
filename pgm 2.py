def  showCounts(S):
    d={}
    for i in range(len(S)):
        if S[i] not in d:
            d[S[i]]=[]
        d[S[i]].append(i)
    return d
S=input("Enter a string: ")
print(showCounts(S))
            