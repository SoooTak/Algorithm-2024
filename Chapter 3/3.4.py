# 202311388 김민상
def dfs(graph, start, visited) :
    if start not in visited :
        visited.add(start)
        print(start, end='')
        nbr = graph[start] - visited
        for v in nbr :
            dfs(graph, v, visited)
            
mygraph = { "A" : {"C", "B"}, 
           "B" : {"A", "D"}, 
           "C" : {"A", "D", "E"}, 
           "D" : {"B", "C", "F"}, 
           "E" : {"C", "G", "H"},
           "F" : {"D"}, 
           "G" : {"E", "H"}, 
           "H" : {"E", "G"}
          }

mygraph2 = {"A" : {"B", "C", "D"}, "B" : {"A"}, "C" : {"A", "D"}, "D" : {"A", "C"}}

print("DFS : ", end='')
dfs(mygraph2, "A", set())
print()
dfs(mygraph, "A", set())