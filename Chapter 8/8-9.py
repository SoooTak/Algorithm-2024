#202311388 김민상
import heapq
def heap_tree(freq, label) :
    n = len(freq)
    h = []
    for i in range(n) :
        heapq.heappush(h, (freq[i], label[i]))
    
    for i in range(1, n) :
        e1 = heapq.heappop(h)
        e2 = heapq.heappop(h)
        heapq.heappush(h, (e1[0] + e2[0], e1[1] + e2[1]))
        print(e1, "+", e2)
    print(heapq.heappop(h))

label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
freq = [24, 3, 8, 10, 33, 6, 4, 12]
heap_tree(freq, label)