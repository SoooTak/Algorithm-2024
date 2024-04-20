#202311388 김민상
def not_error(g, v, pos, path): 
 if g[ path[pos-1] ][v] == 0:
    return False
 for vertex in path: 
    if vertex == v: 
        return False
 return True
def recur(g, path, pos): 
    n = len(g)
    if pos == n:
        if g[path[pos-1]][path[0]] == 1: 
            return True
        else: 
            return False
    for v in range(1, n): 
        if not_error(g, v, pos, path) == True: 
            path[pos] = v 
            if recur(g, path, pos+1) == True: 
                 return True
            path[pos] = -1
    return False
def cycle(g): 
    n = len(g)
    path = [-1] * (n+1) 
    path[0] = path[n] = 0
 
    if recur(g, path, 1) == False: 
        print("해밀토니안 사이클이 없음")
        return False
    else :
        print("해밀토니안 사이클: ", path) 
        return True

g1 = [ [0, 1, 0, 1, 0],
 [1, 0, 1, 1, 1], 
 [0, 1, 0, 0, 1],
 [1, 1, 0, 0, 1], 
 [0, 1, 1, 1, 0], ] 
cycle(g1)