# Last updated: 28.11.2025, 20:48:35
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        res_head = ListNode(-1)
9        curr = res_head
10        while list1 and list2:
11            #print(list1.val,list2.val)
12            if list1.val<list2.val:
13                curr.next = list1
14                list1 = list1.next
15                curr = curr.next
16            else:
17                curr.next = list2
18                list2 = list2.next
19                curr = curr.next
20        if list1:
21            curr.next = list1
22        if list2:
23            curr.next = list2
24        return res_head.next