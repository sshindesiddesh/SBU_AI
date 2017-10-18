#do not modify the function names
#You are given L and M as input
#Each of your functions should return the minimum possible L value alongside the marker positions
#Or return -1,[] if no solution exists for the given L
def check_constraints(V, L, M):
    if (not V):
        return 0;
    if (len(V) != M):
        return 0;
    if (len(V) > (len(set(V)))):
        return 0;
    return 1

def is_consistent(d, V, addist, Dist):
    #print "d-c", d
    #print "V-c", V
    #print "dist-c", dist
    
    for i in range(0, len(V)):
        di = abs(d - V[i])
        if di in Dist or di in addist:
            addist = []
            return 0
        else :
            addist.append(di)
    return 1

def forward_check(d, V, D, adddist, rem):
    #print "FC:adddist:",adddist
    #print "FC:D:",D
    #print "FC:V:",V
    
    for v in V:
        for di in adddist:
            if ((v + di) in D):
                rem.append(v + di)
                D.remove(v + di)

def rec_BT(L, M, V, D, Dist):
    print "V:",V
    print "D:",D
    if (check_constraints(V, L, M)):
        return 1
    # condition to check if all the variables are assigned
    #if (len(V < (M - 1)))
    for d in D :
        print "d:",d
        adddist = []
        rem = []
        if (is_consistent(d, V, adddist, Dist)):
            # Assign value to a variable from domain
            V.append(d)
            # Remove d from possible Domains
            D.remove(d)
            
            # Call recursively to assign further variables from the domain
            for i in adddist:
                Dist.append(i)

            print "Dist 1:", Dist
            print "V1:",V
            print "D1:",D
            forward_check(d, V, D, adddist, rem)
            print "D:",D
            print "rem:",rem

            if (len(V) + len(D)) >= M :
                if rec_BT(L, M, V, D, Dist):
                    return 1
            print "BT:V1:",V
            print "BT:D:",D
            print "BT:rem:",rem
            for di in rem:
                    D.append(di)
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
BT (11, 5)
ts1 = time.time()
print ts1-ts
