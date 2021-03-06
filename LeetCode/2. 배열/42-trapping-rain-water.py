# https://leetcode.com/problems/trapping-rain-water/

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
from collections import defaultdict
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # n이 0이면 0 출력
        if not height:
            return 0

        water_volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            # 투포인터가 위치한 곳의 수면 측정
            left_max, right_max = max(height[left], left_max), max(
                height[right], right_max)

            # 더 높은 쪽을 향해 투포인터 이동
            # left와 right 중 수면이 더 낮은 곳의 물 부피 구하기
            if left_max <= right_max:
                water_volume += left_max - height[left]
                left += 1
            else:
                water_volume += right_max - height[right]
                right -= 1

        return water_volume
