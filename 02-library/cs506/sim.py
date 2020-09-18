def euclidean_dist(x, y):
    return minkowSki_dist(x, y, 2)

def manhattan_dist(x, y):
    return minkowSki_dist(x, y, 1)

def jaccard_dist(x, y):
    # sanity check
    sanity_res = sanity_check(x, y)
    if sanity_res:
        raise sanity_res
    
    # calculate distance
    length = len(x)
    same = 0
    for i in range(length):
        same += 1 if x[i]==y[i] else 0
    return 1-same/length

def cosine_sim(x, y):
    import math
    # sanity check
    sanity_res = sanity_check(x, y)
    if sanity_res:
        raise sanity_res
    
    # calculate distance
    sumaa, sumab, sumbb = 0, 0, 0
    for i in range(len(x)):
        a = x[i]; b = y[i]
        sumaa += a*a
        sumbb += b*b
        sumab += a*b
    return sumab/math.sqrt(sumaa*sumbb)

# Feel free to add more
def sanity_check(x, y):
    if type(x)!=type([]) or type(y)!=type([]):
        return TypeError("x or y is not a list")
    if len(x)==0 or len(y)==0:
        return ValueError("lengths must not be zero")
    if len(x)!=len(y):
        return ValueError("lengths must be equal")

def minkowSki_dist(x, y, p):
    ## sanity_check
    # for p
    if type(p)!=type(int()):
        raise TypeError("p should be an inteager")
    if not p>=1:
        raise ValueError("inteager p should be larger or equal than 1")
    # for x and y
    sanity_res = sanity_check(x, y)
    if sanity_res:
        raise sanity_res
    
    # calculate distance
    length = len(x)
    squared_sum = 0
    for i in range(length):
        squared_sum += pow(abs(x[i]-y[i]), p)
    return pow(squared_sum, 1/p)
