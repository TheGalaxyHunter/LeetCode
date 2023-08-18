# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # return self.first_solution(head)
        # return self.second_solution(head)
        return self.third_solution(head)

    def first_solution(self, head: ListNode) -> ListNode:
        new_head = None
        temp = head

        while temp is not None:
            node = ListNode(temp.val)
            node.next = new_head
            new_head = node
            temp = temp.next

        return new_head

    def second_solution(self, head: ListNode) -> ListNode:
        return self.recursive(head, None)
    
    def recursive(self, head: ListNode, root: ListNode) -> ListNode:
        if head is None:
            return root

        next = head.next
        head.next = root

        return self.recursive(next, head)

    def third_solution(self, head: ListNode) -> ListNode:
        root = None

        while head is not None:
            next_node = head.next
            head.next = root
            root = head
            head = next_node

        return root
    
sol = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head = sol.reverseList(head)
while head is not None:
    print(head.val, end=" -> ")
    head = head.next
print("None")
        