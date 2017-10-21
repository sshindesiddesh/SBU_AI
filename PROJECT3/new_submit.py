#do not modify the function names
#You are given L and M as input
#Each of your functions should return the minimum possible L value alongside the marker positions
#Or return -1,[] if no solution exists for the given L

flag = 0

# Check if all constraints are satisfied
def check_constraints(V, L, M):
    if (len(V) != M):
        return 0;
    return 1

# Function to check if addition of new variable is consistent
def is_consistent(d, V, addist, Dist):
    for i in range(0, len(V)):
        di = abs(d - V[i])
        if di in Dist or di in addist:
            addist = []
            return 0
        else :
            addist.append(di)
    return 1

# Recusrsive Back Tracking Function
def rec_BT(L, M, V, D, Dist):
    # Check if all constraint are satisfied
    if (check_constraints(V, L, M)):
	global flag
	flag = 1
        return 1

    # For all d in domain
    for d in D:
	if (flag == 1):
		return 0;
        # List to store newly calculated distances
        adddist = []

	# Check if d is consistent with current assignments
        if (is_consistent(d, V, adddist, Dist)):
            # Assign value to a variable from domain
            V.append(d)
            # Remove d from possible Domains
            D.remove(d)

            # Add the newly calculated distances to the distance list
            for i in adddist:
                Dist.append(i)

            # Call recursively to assign further variables from the domain
	    if rec_BT(L, M, V, D, Dist):
	        return 1

            # Remove distances specific the variable assignment d 
            for di in adddist :
                Dist.remove(di)

            # Remove assigned value to the variable
            V.remove(d)
            # Add the domain to possible domains
            D.append(d)
    return 0

#Your backtracking function implementation
def call_BT(L, M, var):
    # List for Domain
    domain = []
    # List for calculated distances
    dist = []
    
    # Assign 0 and L 
    var.append(0)
    var.append(L)

    # Add L to distance
    dist.append(L)

    # Populate possible domains
    for i in range(1, L):
        domain.append(i)
        
    # Call recursive BT 
    rec_BT(L, M, var, domain, dist)
    var.sort()
    #print var
    if (var):
        return L, var
    return -1,[]

# Forward Checking
def forward_check(d, V, D, adddist, rem):
    for v in V:
        for di in adddist:
            if ((v + di) in D):
                rem.append(v + di)
                D.remove(v + di)

# Recusrsive Back Tracking Function with forward checking
def rec_FC(L, M, V, D, Dist):
    # Check if all constraint are satisfied
    if (check_constraints(V, L, M)):
	global flag
	flag = 1
        return 1

    # For all d in domain
    for d in D :
	if (flag == 1):
		return 0;
        # List to store newly calculated distances
        adddist = []
        # List to domain values rejected by FC
        rem = []

	# Check if d is consistent with current assignments
        if (is_consistent(d, V, adddist, Dist)):
            # Assign value to a variable from domain
            V.append(d)
            # Remove d from possible Domains
            D.remove(d)

            # Add the newly calculated distances to the distance list
            for i in adddist:
                Dist.append(i)

            # 
            forward_check(d, V, D, adddist, rem)
            # Call recursively to assign further variables from the domain
	    if rec_FC(L, M, V, D, Dist):
	        return 1

            # Remove domain values incdicated by FC
            for di in rem:
                    D.append(di)

            # Remove distances specific the variable assignment d 
            for di in adddist :
                Dist.remove(di)

            # Remove assigned value to the variable
            V.remove(d)
            # Add the domain to possible domains
            D.append(d)
    return 0

#Your backtracking+Forward checking function implementation
def call_FC(L, M, var):
    # List for Domain
    domain = []
    # List for variable
    #var = []
    # List for calculated distances
    dist = []
    
    # Assign 0 and L 
    var.append(0)
    var.append(L)

    # Add L to distance
    dist.append(L)

    # Populate possible domains
    for i in range(1, L):
        domain.append(i)

    # Call recursive BT 
    rec_FC(L, M, var, domain, dist)
    var.sort()
    #print var
    if (var):
        return L, var
    return -1,[]

#Bonus: backtracking + constraint propagation
def CP(L, M):
    "*** YOUR CODE HERE ***"
    return -1,[]

#Your backtracking+Forward checking function implementation
def FC(L, M):
    global flag
    flag = 0
    var = [0]
    l = L
    ans = [-1, []]
    while (var):
        var = []
    	call_FC(l, M, var)
        #print var
        if (len(var) > 2 or (M == 2 and l > 0)):
    	    var.sort()
            ans[1] = var
    	    l = var[len(var) - 1]
            ans[0] = l
            l = l - 1
        else:
            break
    return ans

#Your backtracking+Forward checking function implementation
def BT(L, M):
    global flag
    flag = 0
    var = [0]
    l = L
    ans = [-1, []]
    while (var):
        var = []
    	call_BT(l, M, var)
        #print var
        if (len(var) > 2 or (M == 2 and l > 0)):
    	    var.sort()
            ans[1] = var
    	    l = var[len(var) - 1]
            ans[0] = l
            l = l - 1
        else:
            break
    return ans

import time
ts = time.time()
print FC (55, 10)
ts1 = time.time()
print ts1-ts
ts = time.time()
#print BT (44, 9)
ts1 = time.time()
print ts1-ts
