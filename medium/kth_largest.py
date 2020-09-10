class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # make a min heap of the largest K element from nums
        # if value < top, return top
        # if value > top, put value on the top and heapify the top K element
        if not nums: self.nums=[]
        else:
            pq=[]
            # Min heap of length k
            for i in nums:
                if len(pq)< k:
                    heapq.heappush(pq,i)
                else:
                    smallest = heapq.heappop(pq)
                    if i > smallest:
                        heapq.heappush(pq,i)
                    else:
                        heapq.heappush(pq,smallest)
            self.nums=pq



    def add(self, val: int) -> int:
        if len(self.nums)<self.k:
            heapq.heappush(self.nums,val)
            return self.nums[0]
        temp = self.nums[0]
        if val > temp:
            heapq.heappop(self.nums)
            heapq.heappush(self.nums,val)
        
        return self.nums[0]