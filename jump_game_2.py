def jump(self, nums: List[int]) -> int:
    _len = len(nums)
    if _len <= 1: return 0
    stop_pos = 0
    max_des = 0
    jumps = 0
    for idx in range(_len-1):
        max_des = max(max_des, idx+nums[idx])
        if stop_pos == idx:
            stop_pos = max_des
            jumps += 1
            if max_des >= _len-1:
                return jumps
        if max_des >= _len-1:
            return jumps+1
