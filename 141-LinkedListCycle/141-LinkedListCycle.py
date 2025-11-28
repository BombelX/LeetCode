# Last updated: 28.11.2025, 20:16:11
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        if head == None or head.next == None:
10            return False
11        
12        rabbit = head
13        turtle = head
14
15        while rabbit and  rabbit.next and rabbit.next.next :
16            rabbit,turtle = rabbit.next.next,turtle.next
17            if rabbit == turtle:
18                return True
19        return False
20