# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy = ListNode()
        slow = head
        fast = head

        while fast:
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                break
            slow = slow.next
        
        if fast == head:
            return head
        
        sec_half = slow.next
        slow.next = None

        # reverse sec_half
        sec_half = self.reverseList(sec_half)

        l1 = head
        while l1 and sec_half:
            next = l1.next
            l1.next = sec_half
            sec_half = sec_half.next
            l1 = l1.next
            l1.next = next
            l1 = l1.next

    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            next_n = curr.next
            curr.next = prev
            prev = curr
            curr = next_n
        head = prev

        return head
            
sol = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol.reorderList(head)
while head is not None:
    print(head.val, end=" -> ")
    head = head.next
print("None")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
sol.reorderList(head)
while head is not None:
    print(head.val, end=" -> ")
    head = head.next
print("None")

head = ListNode(1, ListNode(2, ListNode(3)))
sol.reorderList(head)
while head is not None:
    print(head.val, end=" -> ")
    head = head.next
print("None")

head = ListNode(1, ListNode(2))
sol.reorderList(head)
while head is not None:
    print(head.val, end=" -> ")
    head = head.next
print("None")

head = ListNode(1)
sol.reorderList(head)
while head is not None:
    print(head.val, end=" -> ")
    head = head.next
print("None")

head = ListNode()
sol.reorderList(head)
while head is not None:
    print(head.val, end=" -> ")
    head = head.next
print("None")

head = None
sol.reorderList(head)
while head is not None:
    print(head.val, end=" -> ")
    head = head.next
print("None")
