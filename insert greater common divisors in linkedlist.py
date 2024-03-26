class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp2 = head
        while head.next:
            n1 = head.val
            n2 = head.next.val
            n3 = math.gcd(n1,n2)
            tmp = ListNode()
            tmp.val = n3
            tmp.next = head.next
            head.next = tmp
            head = head.next.next
        return tmp2