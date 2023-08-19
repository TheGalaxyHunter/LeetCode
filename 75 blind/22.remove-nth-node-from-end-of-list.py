# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        arr = []

        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        arr.pop(len(arr)-n)

        new_head = ListNode()
        nxt = new_head
        for i in arr:
            nxt.next = ListNode(i)
            nxt = nxt.next

        return new_head.next


sol = Solution()
print("Solution to [1,2,3,4,5] with n=2:", end=" ")
head = sol.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
while head is not None:
    print(head.val, end=" -> ")
    head = head.next
print("None")

print("Solution to [1] with n=1:", end=" ")
head = sol.removeNthFromEnd(ListNode(1), 1)
while head is not None:
    print(head.val, end=" -> ")
    head = head.next
print("None")

print("Solution to [1,2] with n=1:", end=" ")
head = sol.removeNthFromEnd(ListNode(1, ListNode(2)), 1)
while head is not None:
    print(head.val, end=" -> ")
    head = head.next
print("None")

print("Solution to [1,2] with n=2:", end=" ")
head = sol.removeNthFromEnd(ListNode(1, ListNode(2)), 2)
while head is not None:
    print(head.val, end=" -> ")
    head = head.next
print("None")

print("Solution to [1,2,3] with n=1:", end=" ")
head = sol.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3))), 1)
while head is not None:
    print(head.val, end=" -> ")
    head = head.next
print("None")