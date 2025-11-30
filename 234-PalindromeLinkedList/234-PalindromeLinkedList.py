# Last updated: 30.11.2025, 23:55:42
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def isPalindrome(self, head: Optional[ListNode]) -> bool:
8        
9        def reverse(head):
10            prev = None
11            while head:
12                nxt = head.next
13                head.next = prev
14                prev = head
15                head = nxt
16            return prev
17
18        if head is None:
19            return False
20        n = 0
21        curr = head
22        while curr:
23            curr = curr.next
24            n+=1
25
26        mid = n//2
27        mid_pointer = None
28        curr = head
29        ind = 0
30        while curr:
31            if ind == mid:
32                mid_pointer = curr
33                break
34            ind+=1
35            curr = curr.next
36        end_pointer = reverse(mid_pointer)
37        for i in range(mid):
38            if end_pointer and head:
39                if end_pointer.val == head.val:
40                    end_pointer = end_pointer.next
41                    head = head.next
42                else: return False
43            else:
44                return False
45        return True
46            
47        