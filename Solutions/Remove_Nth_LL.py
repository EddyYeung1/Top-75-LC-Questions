'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''

'''
Solution 1: Get the length of the linked list first then stop one less than n so that you stop just before you reach that element. We want to stop just before it so that we can set the next pointer past it and essential "erase" that node.
Solution 2: There is apparently a one pass solution for this, but the LC community begs to differ. Since they seem to not agree with the one pass solution I'm not gonna do it here. You can look at the solution on lc to see it.
'''


def removeNthFromEnd(self, head, n):
    lenOfList = 0
    dummy = head  # keep a pointer to the head otherwise you

    while dummy:  # get length of list
        dummy = dummy.next
        lenOfList += 1

    ans = head

    if lenOfList == n:  # the below for loop does not work if the length of the list is the size of n
        return head.next

    for i in range(lenOfList-n-1):  # this stops 1 index before n
        ans = ans.next

    if ans.next.next:  # make sure we can overwrite the deleted node with its next
        ans.next = ans.next.next
    else:  # the deleted node is at the end of the list
        ans.next = None

    return head
