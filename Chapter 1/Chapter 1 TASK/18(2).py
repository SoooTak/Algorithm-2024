#202311388 김민상
#Chapter 1
#문제 18-(2)_단순연결리스트 구조
class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

def create_linked_list(num_nodes):
    head = None
    tail = None

    for _ in range(num_nodes):
        data = input(f"노드 #{_+1} 데이터 : ")
        new_node = Node(data)

        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.link = new_node
            tail = new_node

    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.link
    print("None")

if __name__ == "__main__":
    num_nodes = int(input("노드의 개수 : "))
    linked_list_head = create_linked_list(num_nodes)
    print("리스트의 내용 :")
    print_linked_list(linked_list_head)

