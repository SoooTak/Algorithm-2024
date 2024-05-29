#202311388 김민상
choice = '\0'
MAX = 100
table = [None] * MAX

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert(str) :
    id = hash(str[0]) % MAX
    if table[id] == None :
        table[id] = []
        table[id].append(list(str))
    else :
        table[id].append(list(str))
    return

def delete(str) :
    id = hash(str) % MAX
    if table[id] == None :
        print(f"{str}은 테이블에 없음")
    else :
        for i in range(len(table[id])) :
            if table[id][i][0] == str :
                table[id].pop(i)
                if table[id] == [] :
                    table[id] = None
                print(f"{str} 삭제 완료")
                print()
                return 
        print(f"{str}은 테이블에 없음")
    return

def search(str) :
    id = hash(str) % MAX
    state = 0
    if table[id] == None :
        print(f"{str}은 테이블에 없음")
    else :
        for i in range(len(table[id])) :
            if table[id][i][0] == str :
                print(table[id][i])
                state = 1
        if state == 0 :
            print(f"{str}은 테이블에 없음")
    print()
    return

while (choice != 'x') :
    word = []
    print("[단어장] 추가 : i    삭제 : d     검색 : s   출력 : p    종료 : x   ", end=" ")
    choice = input("")
    
    if(choice == 'i') :
        str = input("단어 : ")
        str_mean = input("의미 : ")
        word.append(str)
        word.append(str_mean)
        insert(word)
        
    elif(choice == 'd') :
        del_str = input("삭제할 단어 : ")
        delete(del_str)
        
    elif(choice == 's') :
        search_str = input("검색할 단어 : ")
        search(search_str)
        
    elif(choice == 'p') :
        print()
        for i in range(MAX) :
            if(table[i] != None) :
                print(table[i])
        print()