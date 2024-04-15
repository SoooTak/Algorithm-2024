# 202311388 김민상
import queue # 큐 사용
def bfs(graph, start) :
    visited = {start}
    que = queue.Queue()
    que.put(start)
    while not que.empty() :
        v = que.get()
        print(v, end= ' ')
        nbr = graph[v] - visited
        for u in nbr :
            visited.add(u)
            que.put(u)

mygraph3 = { "A" : {"B", "C"}, 
           "B" : {"A", "D"}, 
           "C" : {"A", "D", "E"}, 
           "D" : {"B", "C", "F"}, 
           "E" : {"C", "G", "H"},
           "F" : {"D"}, 
           "G" : {"E", "H"}, 
           "H" : {"E", "G"}
          }

print("BFS : ",end=' ')
bfs(mygraph3, "A")
print()

mygraph2 = {"A" : {"B", "C", "D"}, "B" : {"A"}, "C" : {"A", "D"}, "D" : {"A", "C"}}
bfs(mygraph2, "A")