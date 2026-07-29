class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        while l < r:
            combine = numbers[l]+ numbers[r]
            if combine == target:
                return [l+1,r+1] #problem wnated 1 indexed for some reason
            elif combine > target: #need smaller so right go left
                r -= 1
            elif combine < target: #need bigger so left go right
                l += 1
        