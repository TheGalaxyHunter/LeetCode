# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # return self.first_solution(head)
        return self.second_solution(head)
    
    def first_solution(self, head: ListNode) -> bool:
        curr = head
        hset = set()
        
        while curr:
            if curr in hset:
                return True
            hset.add(curr)
            curr = curr.next

        return False

    def second_solution(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
    

sol = Solution()
head = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
head.next.next.next.next = head.next
print(sol.hasCycle(head))

head = ListNode(1, ListNode(2))
head.next.next = head
print(sol.hasCycle(head))

head = ListNode(1)
print(sol.hasCycle(head))
