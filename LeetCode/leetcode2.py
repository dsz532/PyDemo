# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        counter=0
        cur=l1
        sum=0
        while cur!=None:
            sum+=cur.val*(10**counter)
            cur=cur.next
            counter+=1
        cur=l2
        counter=0
        while cur!=None:
            sum+=cur.val*(10**counter)
            cur=cur.next
            counter+=1
        counter=1
        head=ListNode(sum%(10**counter))
        pre=head
        while sum//(10**counter)!=0:
            l3=ListNode()
            l3.val=sum//(10**counter)%10
            l3.next=None
            pre.next=l3
            pre=l3
            counter+=1
        return head