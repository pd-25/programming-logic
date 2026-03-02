#detect if there is cycle in linklist
# this means if any of node points to any previous node


# Wei will use 2 pointer
from typing import Optional
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next= next
        

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(6)
head.next.next.next.next.next = head.next.next

def hasCycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
        
    return False
    
print(hasCycle(head))


