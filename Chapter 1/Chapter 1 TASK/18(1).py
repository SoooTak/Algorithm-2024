#202311388 김민상
#Chapter 1
#문제 18-(1)_파이썬 리스트 알고리즘

list = []
node = int(input("노드의 개수 : "))
for i in range(0, node) :
    list.append(int(input(f"노드 #{i+1} : ")))
    
print(f"리스트의 내용: {list}") 