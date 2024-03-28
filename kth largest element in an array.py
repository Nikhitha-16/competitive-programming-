class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
        i = len(nums) - k
        while i>0:
            heapq.heappop(minHeap)
            i-=1
        return minHeap[0]