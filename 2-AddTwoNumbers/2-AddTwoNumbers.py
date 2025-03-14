# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#    def revert(l_list):
#        if l_list is None:
#            return l_list
#        prev = None
#        while l_list is not None:
#            tmp = l_list.next
#            l_list.next = prev
#            prev = l_list
#            l_list = tmp
#        return prev

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #l1,l2 = revert(l1),revert(l2)
        step = 0
        summ = 0
        r = 0
        while l1 is not None and l2 is not None :
            tmp = l1.val + l2.val+r
            summ += (tmp%10)*10**step
            r = tmp//10
            step+=1
            l1,l2 = l1.next,l2.next
        end = None
        if l1 is None:
            end = l2
        elif l2 is None:
            end = l1
        else:
            if r >0 :
                sum += r*10**step
        while end is not None:
            tmp = end.val +r
            summ += (tmp%10)*10**step
            r = tmp//10
            step+=1
            end = end.next
        if r>0:
            summ += r*10**step
        start = None
        head = None
        if summ == 0:
            return ListNode(summ)
        while summ>0:
            if head is None:
                head=ListNode(summ%10)
                start = head
            else:
                head.next = ListNode(summ%10)
                head = head.next
            summ//=10
        return start