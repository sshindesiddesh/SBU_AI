#do not modify the function names
#You are given L and M as input
#Each of your functions should return the minimum possible L value alongside the marker positions
#Or return -1,[] if no solution exists for the given L
def check_constraints(V, L, M):
    if (not V or len(V) != M or (L not in V)):
        return 0
    
    dist = []
    for i in range(0, M):
        for j in range(i + 1, M):
            d = abs(V[j] - V[i])
            if d not in dist:
                dist.append(d);
            else :
                return 0
    return 1

def is_consistent(d, V, addist, Dist):
    #print "d-c", d
    #print "V-c", V
    #print "dist-c", dist
    
    for i in range(0, len(V)):
        di = abs(d - V[i])
        if di in Dist:
            addist = []
            return 0
        else :
            addist.append(di)
    
    return 1

"""
    if (len(V) == 0):
        return 1
    V.append(d)
    for i in range(0, len(V)):
        for j in range(i + 1, len(V)):
            di = abs(V[j] - V[i])
            if di not in dist:
                dist.append(di);
            else :
                V.remove(d)
                return 0
    V.remove(d)
    return 1
"""

def forward_check(V,D,dist,rem):
    #print "dist:",dist
    #print "D:",D
    for i in range(0,len(V)):
        for j in range(0,len(dist)):
            di = V[i]+dist[j]
            if di in D:
                rem.append(di)
                D.remove(di)

def rec_BT(L, M, V, D, Dist):
    #print "V:",V
    #print "D:",D
    if (check_constraints(V, L, M)):
        return 1
    # condition to check if all the variables are assigned
    #if (len(V < (M - 1)))
    for d in D :
        #print "d:",d
        adddist = []
        rem = []
        if (is_consistent(d, V, adddist, Dist)):
            # Assign value to a variable from domain
            V.append(d)
            # Remove d from possible Domains

            D.remove(d)
            #print "V1:",V
            #print "D1:",D
            #forward_check(V,D,dist,rem)
            #print "D:",D
            #print "rem:",rem

            # Call recursively to assign further variables from the domain
            for i in adddist :
                Dist.append(i)

            if rec_BT(L, M, V, D, Dist) :
                return 1
            #print "BT:V1:",V
            #print "BT:D:",D
            #print "BT:rem:",rem
            #for di in rem:
            #        D.append(di)
            # Remove assigned value to the variable
        
            for i in adddist :
                Dist.remove(i)

            V.remove(d)
            # Add the domain to possible domains
            D.append(d)


    
      
    return 0

#Your backtracking function implementation
def BT(L, M):
    domain = []
    var = []
    dist = []
    "*** YOUR CODE HERE ***"
    var.append(0)
    var.append(L)
    dist.append(L)
    for i in range(1, L):
        domain.append(i)
        
    rec_BT(L, M, var, domain, dist)
    var.sort()
    print var
    return -1,[]

#Your backtracking+Forward checking function implementation
def FC(L, M):
    "*** YOUR CODE HERE ***"
    
    return -1,[]

#Bonus: backtracking + constraint propagation
def CP(L, M):
    "*** YOUR CODE HERE ***"
    return -1,[]

print "Hello "
import time
ts = time.time()
BT (72, 11)
ts1 = time.time()
print ts1-ts
