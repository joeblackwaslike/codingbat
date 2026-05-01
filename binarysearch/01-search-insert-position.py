"""
# [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/description/?envType=problem-list-v2&envId=binary-search)

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with`O(log n)` runtime complexity.

**Example 1:**
```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

**Example 2:**
```
Input: nums = [1,3,5,6], target = 2
Output: 1
```

**Example 3:**
```
Input: nums = [1,3,5,6], target = 7
Output: 4
```

**Constraints:**
- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` contains **distinct**  values sorted in **ascending**  order.
- `-10^4 <= target <= 10^4`
"""


def searchInsert(nums: list[int], target: int) -> int:
    # left = 0
    # right = len(nums) - 1

    # while left <= right:
    #     mid = (left + right) // 2

    #     if nums[mid] == target:
    #         return mid
    #     if nums[mid] > target:
    #         right = mid - 1
    #     else:
    #         left = mid + 1

    # return left

    # Pathrise template
    left = 0
    right = len(nums) - 1

    while left + 1 < right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return left


import pytest


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
    ],
)
def test(nums, target, expected):
    result = searchInsert(nums, target)
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__])
