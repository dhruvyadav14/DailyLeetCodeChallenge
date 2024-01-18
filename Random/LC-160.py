# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None

        lenA = 0
        lenB = 0
        pa = headA # 2 pointers
        pb = headB
        while pa.next:
            pa=pa.next
            lenA+=1
        while pb.next:
            pb=pb.next
            lenB+=1
                
        diff = abs(lenA-lenB)
        headAcopy = headA
        headBcopy = headB
        if lenA>lenB:
            #move A up by some spots
            for i in range(diff):
                headAcopy=headAcopy.next
        else:
            for i in range(diff):
                headBcopy=headBcopy.next
            
        while headBcopy is not headAcopy:
            headAcopy = headAcopy.next
            headBcopy = headBcopy.next
        
        return headBcopy