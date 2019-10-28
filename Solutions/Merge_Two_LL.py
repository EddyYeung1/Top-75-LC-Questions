'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

'''
Solution: Create a dummy node that creates the new Linked Lists that adds nodes appropriately as it traverses both of l1 and l2. O(N) Time O(1) space 
'''


def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummyNode = ListNode(0)
    headPtr = dummyNode

    while l1 and l2:
        if l1.val <= l2.val:
            dummyNode.next = l1
            l1 = l1.next
        else:
            dummyNode.next = l2
            l2 = l2.next
        dummyNode = dummyNode.next

    if l1:
        dummyNode.next = l1

    if l2:
        dummyNode.next = l2

    return headPtr.next
