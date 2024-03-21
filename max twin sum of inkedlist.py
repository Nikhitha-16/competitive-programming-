class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        maxsum = lst[0]+ lst[-1]
        i = 0
        j = len(lst)-1
        while i<j:
            if(lst[i]+ lst[j]> maxsum):
                maxsum = lst[i]+ lst[j]
            i+=1
            j-=1
        return maxsum