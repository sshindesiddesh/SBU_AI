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

def is_consistent(d, V):
    if (len(V) == 0):
        return 1
    V.append(d)
    dist = []
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

def rec_BT(L, M, V, D):
    if (check_constraints(V, L, M)):
        return 1
    # condition to check if all the variables are assigned
    #if (len(V < (M - 1)))
    for d in D :
        if (is_consistent(d, V)):
            # Assign value to a variable from domain
            V.append(d)
            # Remove d from possible Domains
            D.remove(d)
            # Call recursively to assign further variables from the domain
            if rec_BT(L, M, V, D) :
                return 1
            # Remove assigned value to the variable
            V.remove(d)
            # Add the domain to possible domains
            D.append(d)
    
      
    return 0

#Your backtracking function implementation
def BT(L, M):
    domain = []
    var = []
    "*** YOUR CODE HERE ***"
    for i in range(0, L + 1):
        domain.append(i)
        
    rec_BT(L, M, var, domain)
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
BT (70, 10)
