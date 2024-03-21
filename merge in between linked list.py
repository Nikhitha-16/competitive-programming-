class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        res = list1
        list2_tmp = list2
        count = 0
        while count < a - 1:
            list1 = list1.next
            count+=1
        list1_tmp = list1.next
        list1.next = list2
        while count < b:
            list1_tmp = list1_tmp.next
            count+=1
        while list2_tmp.next:
            list2_tmp = list2_tmp.next
        list2_tmp.next = list1_tmp
        return res