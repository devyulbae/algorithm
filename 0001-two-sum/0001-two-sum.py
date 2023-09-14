class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):   #num 길이만큼
            i_val = nums[i]
            for j in range(1, len(nums)):
                j_val = nums[j]
                if i==j:
                    break
                if i_val + j_val == target:
                    output.append(i)
                    output.append(j)
                    return output
                    