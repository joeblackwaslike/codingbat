"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single points.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""

from typing import List


def restoreIpAddresses(s: str) -> List[str]:
    def dfs(idx, path, segmentNum):
        if segmentNum == 4 and idx == len(s):
            allIpAddresses.append(".".join(path))
            return
        elif segmentNum == 4 or idx == len(s):
            return

        windowSize = 1
        while windowSize <= 3 and idx + windowSize <= len(s):
            subStr = s[idx : idx + windowSize]
            if int(subStr) > 255 or windowSize >= 2 and s[idx] == "0":
                break
            path[segmentNum] = subStr
            dfs(idx + windowSize, path, segmentNum + 1)
            path[segmentNum] = ""

            windowSize += 1

    allIpAddresses = []
    path = []
    dfs(0, path, 1)
    return allIpAddresses


import pytest


def test_solution():
    result = restoreIpAddresses("25525511135")
    assert sorted(result) == sorted(["255.255.11.135", "255.255.111.35"])


if __name__ == "__main__":
    pytest.main([__file__])
