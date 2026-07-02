class NumArray:

    def __init__(self, nums: List[int]):
        self.list1=[]
        sum1=0
        #self.list1.append(0)
        for n in nums:
            sum1+=n
            self.list1.append(sum1)

        

    def sumRange(self, left: int, right: int) -> int:
        right=self.list1[right]
        left=self.list1[left-1] if left>0 else 0
        return right-left
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)