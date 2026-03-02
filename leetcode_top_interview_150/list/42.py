# https://leetcode.com/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        p_left = 0
        p_right = n-1
        max_p_left = height[p_left]
        max_p_right = height[p_right]
        total = 0

        while p_left < p_right:
            if height[p_left] < height[p_right]:
                p_left += 1
                if height[p_left] > max_p_left:
                    max_p_left = height[p_left]
                
                total += max_p_left - height[p_left]
            else:
                p_right -= 1
                if height[p_right] > max_p_right:
                    max_p_right = height[p_right]
                
                total += max_p_right - height[p_right]
        
        return total
