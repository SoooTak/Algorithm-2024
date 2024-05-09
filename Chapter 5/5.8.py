#202311388 김민상
import math
def distance(p1, p2) :
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def strip_closest(P, d) :
    n = len(P)
    d_min = d
    P.sort(key = lambda point:point[1])
    
    for i in range(n) :
        j = i + 1
        while j < n and (P[j][1] - P[i][1]) < d_min :
            dij = distance(P[i], P[j])
            if dij < d_min :
                d_min = dij
            j+=1
    return d_min

p = [(2,3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
d = 10
print(strip_closest(p, d))