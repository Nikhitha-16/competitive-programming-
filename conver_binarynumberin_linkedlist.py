class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        stack=[]
        while head:
            stack.append(head.val)
            head=head.next
        dec=0
        length=0
        while stack:
            dec=dec+math.pow(2,length)*stack.pop()
            length+=1
        return int(dec