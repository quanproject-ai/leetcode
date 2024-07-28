# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# iteratively
def mergeTwoLists_iteratively(self, l1: ListNode, l2:ListNode)->ListNode:
    dummy = tail = ListNode(0) # 
    while l1 and l2: #iterative each value within the list as long as both lists are not empty
        if l1.val < l2.val: 
            tail.next = l1 #set the next pointer of tail node to the current node of l1
            l1 = l1.next #advances the l1 pointer to the next node in the l1 list
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next #then move the tail to the next node in the tail
    tail.next = l1 or l2 #if one list is finised (i.e. out of elements), the tail points to whichever lists are not empty
    return dummy.next

def mergeTwoLists_recursive(self, l1: ListNode, l2:ListNode)->list:
    if not l1 or not l2: #check either list is empty
        return l1 or l2 #return either list because it is already in ordered (both lists are given as sorted)
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists_inplace_iterative(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists_inplace_iterative(l1, l2.next)
        return l2

# in-place, iteratively        
def mergeTwoLists_inplace_iterative(self, l1: ListNode, l2:ListNode)->ListNode:
    if None in (l1, l2):
        return l1 or l2
    dummy = tail = ListNode(0)
    dummy.next = l1
    while l1 and l2:
        if l1.val < l2.val:
            l1 = l1.next
        else:
            nxt = tail.next
            tail.next = l2
            tmp = l2.next
            l2.next = nxt
            l2 = tmp
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next