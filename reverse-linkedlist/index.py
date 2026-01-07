#Reverse a linked list

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next= next
        

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(6)


def reverse_linkedlist(head: ListNode) -> ListNode:
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
    

current = reverse_linkedlist(head)
while current:
    print(current.value, end=" -> " if current.next else "\n")
    current = current.next