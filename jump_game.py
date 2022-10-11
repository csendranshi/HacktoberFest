def canJump(self, nums: List[int]) -> bool:
    _len = len(nums)
    if _len <=1: return True
    output = False
    end = _len-1
    for idx in range(_len-2, -1, -1):
        output = idx + nums[idx] >= end
        if output: end = idx
    return output
