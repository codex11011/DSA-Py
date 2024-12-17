
# https://leetcode.com/problems/3sum/
def three_sum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()
    n = len(nums)
    i=0
    while i<n-2:
        if i>0 and nums[i]==nums[i-1]:
            i+=1
            continue
        j=i+1
        k=n-1
        while(j<k):
            target = nums[i]+nums[j]+nums[k]
            if target == 0:
                res.append([nums[i], nums[j], nums[k]])
                while j<k and nums[j]==nums[j+1]: j+=1
                while j<k and nums[k]==nums[k-1]: k-=1
                j+=1
                k-=1
            elif target > 0:
                k-=1
            else:
                j+=1
        i+=1
    return res

# https://leetcode.com/problems/3sum-closest/
def three_sum_closest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    diff = float('inf')
    n=len(nums)
    nums.sort()
    i=0
    res = None
    while i<n-2:
        if i>0 and nums[i]==nums[i-1]:
            i+=1
            continue
        j=i+1
        k=n-1
        while j<k:
            s = nums[i]+nums[j]+nums[k]
            if abs(target-s) < diff:
                diff = abs(target-s)
                res = s
            elif target < s:
                k-=1
            else:
                j+=1
        i+=1
    return res

# https://leetcode.com/problems/3sum-smaller/
# Given an array arr of unsorted numbers and a target sum, 
# count all triplets in it such that arr[i] + arr[j] + arr[k] < target 
# where i, j, and k are three different indices. Write a function to 
# return the count of such triplets.

def triplet_with_smaller_sum(arr, target):
    arr.sort()  # Sort the array in ascending order
    count = 0
    
    for i in range(len(arr) - 2):  # Loop through the array
        count += search_pair(arr, target - arr[i], i)
    
    return count

def search_pair(arr, target_sum, first):
    count = 0
    start = first + 1
    end = len(arr) - 1
    
    while start < end:
        if arr[start] + arr[end] < target_sum:
            count += end - start
            start += 1
        else:
            end -= 1
    
    return count



