# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = None
        next = None

        while list1 is not None or list2 is not None:
            print(list1.val if list1 is not None else None, list2.val if list2 is not None else None)
            if list1 is None:
                temp = list2
                list2 = list2.next

            elif list2 is None:
                temp = list1
                list1 = list1.next

            elif list1.val <= list2.val:
                temp = list1
                list1 = list1.next

            elif list1.val > list2.val:
                temp = list2
                list2 = list2.next

            if head is None:
                head = temp
                next = head
                next.next = None
            else:
                next.next = temp
                next = temp

        return head
    
sol = Solution()
head = sol.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4))))
while head is not None:
    print(head.val, end=" -> ")
    head = head.next
print("None")

head = sol.mergeTwoLists(ListNode(), ListNode())
while head is not None:
    print(head.val, end=" -> ")
    head = head.next
print("None")

head = sol.mergeTwoLists(ListNode(), ListNode(0))
while head is not None:
    print(head.val, end=" -> ")
    head = head.next
print("None")

head = sol.mergeTwoLists(ListNode(1), ListNode(0))
while head is not None:
    print(head.val, end=" -> ")
    head = head.next
print("None")

head = sol.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4))))
while head is not None:
    print(head.val, end=" -> ")
    head = head.next
print("None")