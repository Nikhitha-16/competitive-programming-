class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        while head:
            stack.append(head)
            head=head.next
        tmp=len(stack)//2+1
        return stack[tmp-1]