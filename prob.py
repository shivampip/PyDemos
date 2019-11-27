def gridSearch(G, P):
    gh= len(G)
    ph= len(P)
    for i in range(gh-ph+1):
        t= 0
        flag= True
        mi= -1
        for k in range(ph):
            if(P[k] in G[i+t]):
                if(mi==-1):
                    mi= G[i+t].index(P[k])
                elif(G[i+t].index(P[k])!= mi):
                    flag= False 
                    break 
                t+=1
            else: 
                flag= False
                break 
        if(flag):
            return "YES"
    return "NO"



G= ["1 1 2 2", "3 3 4 4", "5 5 6 6"]
P= ["8"]
print(gridSearch(G,P))