class Solution:
    def permute_recr(self, nums, _size, _end, sol, result):
        if  _size == 0:
            result.append(sol)
            return
        for idx in range(_end):
            if -10 <= nums[idx] <= 10:
                tmp = nums[idx]
                nums[idx] = 100
                self.permute_recr(nums, _size-1, _end, sol+[tmp], result)
                nums[idx]  = tmp
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.permute_recr(nums, len(nums), len(nums), [], result)
        return result
