# SLIDING WINDOW

# https://leetcode.com/problems/largest-subarray-length-k/
# Given an array of positive numbers and a positive number K,
# find the maximum sum of any contiguous subarray of size K.
def maxSubarrayOfSizeK(arr: list, k: int) -> int:
    
    n = len(arr)
    currentSum = sum(arr[i] for i in range(k))
    maxSum = currentSum
    
    for i in range(k, n):
        currentSum+=arr[i]
        currentSum-=arr[i-k]
        maxSum = max(maxSum, currentSum)
    
    return maxSum

# https://leetcode.com/problems/minimum-size-subarray-sum/
# Given an array of positive numbers and a positive number S, 
# find the length of the smallest contiguous subarray whose sum i
# s greater than or equal to S.


def smallestSubarrayWithGivenSum(arr, s):
    currentSum = 0
    minlen = float('inf')
    l=0
    n = len(arr)
    
    for r in range(n):
        currentSum += arr[r]
        while currentSum>=s:
            minlen = min(minlen, r-l+1)
            currentSum-=arr[l]
            l+=1
    
    if minlen == float('inf'):
        return 0
    return minlen


# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# Given a string, find the length of the longest substring in it 
# with no more than K distinct characters.
# You can assume that K is less than or equal to the 
# length of the given string.
# longest Substring with k distinct char
# fruits in basket

def longestSubstringWithKdistinct(str, k):
    l=0
    maxlen = 0
    n = len(str)
    mp = {}
    
    for r in range(n):
        
        if str[r] not in mp:
            mp[str[r]] = 1
            while len(mp) > k and l<=r:
                # slide window left
                mp[str[l]]-=1
                if mp[str[l]]==0:
                    mp.pop(str[l])
                l+=1
        else:
            mp[str[r]]+=1
        maxlen = max(maxlen, r-l+1)
    
    return maxlen

# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# length of longest substring with no repeating char
def lengthOfLongestSubstringWithNoRepeatingChar(s: str) -> int:
        l=0
        n = len(s)
        mp = {}
        maxlen = 0

        for r in range(n):
            if s[r] not in mp:
                mp[s[r]]=1
            else:
                mp[s[r]]+=1
                while mp[s[r]]>1:
                    mp[s[l]]-=1
                    if mp[s[l]] == 0:
                        mp.pop(s[l])
                    l+=1
            maxlen = max(maxlen, len(mp))
        return maxlen



# Given an array arr and a number k.
# One can apply a swap operation on the array any number of times,
# i.e choose any two index i and j (i < j) and swap arr[i] , arr[j] . 
# Find the minimum number of swaps required to bring all the numbers less than or 
# equal to k together, i.e. make them a contiguous subarray.

def minSwapToMakeElementTogether(arr, k):
    n = len(arr)
    count_k = sum(x for x in arr if x<=k)
    if count_k==0 or count_k==n:
        return 0

    count_gt_k = sum(arr[i] for i in range(count_k) if arr[i]>k)
    minswap = count_gt_k
    
    for r in range(count_k, n):
        if arr[r]>k: count_gt_k+=1
        if arr[r-count_k]>k: count_gt_k-=1
        minswap = min(minswap, count_gt_k)
    
    return minswap
        

# https://leetcode.com/problems/longest-repeating-character-replacement/        # 
# You are given a string s and an integer k. 
# You can choose any character of the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same
# letter you can get after performing the above operations.

def characterReplacement(s, k):
    n=len(s)
    l=0
    maxrepeatcount = 0
    mp = {}
    maxlen = 0
    
    for r in range(n):
        
        mp[s[r]] = mp.get(s[r], 0) + 1
        
        maxrepeatcount = max(maxrepeatcount, mp[s[r]])
            
        if r - l + 1 - maxrepeatcount > k:
            mp[s[l]] -= 1
            l += 1
        maxlen = max(maxlen, r - l + 1)
    
    return maxlen
            

# https://leetcode.com/problems/max-consecutive-ones-iii/description/
# Given a binary array nums and an integer k, 
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


def longestOnes(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    l = 0
    count_zero = 0
    maxlen = 0
    n = len(nums)

    for r in range(n):
        if nums[r]==0:
            count_zero+=1
        
        while count_zero>k:
            count_zero -= 1 if nums[l]==0 else 0
            l+=1
        maxlen = max(maxlen, r-l+1)
    return maxlen


# https://leetcode.com/problems/permutation-in-string/description/
def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    def all_zero(mp):
        for i in mp:
            if mp[i]!=0:
                return False
        return True

    mp = {}
    
    # window length
    n1 = len(s1)
    n2 = len(s2)
    for i in s1:
        mp[i] = mp.get(i,0) + 1
    
    for i in range(n2):
        if s2[i] in mp:
            mp[s2[i]]-=1
        if i>=n1 and s2[i-n1] in mp:
            mp[s2[i-n1]]+=1
        
        if all_zero(mp):
            return True
    
    return False

# https://leetcode.com/problems/minimum-window-substring/
# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".

def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    n1 = len(t)
    n2 = len(s)
    if n2<n1:
        return ""
    minlen = float('inf')
    
    l=0
    mp={}
    matches=0
    start_index = -1

    for i in t: 
        mp[i] = mp.get(i,0) + 1
    
    # we have all elements
    for r in range(n2):

        if s[r] in mp:
            mp[s[r]]-=1
            if mp[s[r]]==0:
                matches+=1

        while matches==len(mp):
            if minlen > r-l+1:
                minlen = r-l+1
                start_index = l
            if s[l] in mp:
                mp[s[l]]+=1
                if mp[s[l]] > 0:
                    matches-=1
                    l+=1
                    continue    
            l+=1

    if start_index==-1:
        return ""
    return s[start_index:start_index+minlen]
    



# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

from collections import Counter

def findSubstring(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    word_len = len(words[0])
    n = len(words)
    k = word_len * n
    
    # If the length of string is less than the total length of all words, no substrings can match
    if len(s) < k:
        return []

    # Create a frequency map for the words list
    word_count = Counter(words)
    res = []

    # We will check every possible starting index for a substring
    for i in range(word_len):
        left = i
        right = i
        seen = Counter()

        while right + word_len <= len(s):
            # Get the word at the 'right' pointer
            word = s[right:right + word_len]
            right += word_len

            if word in word_count:
                seen[word] += 1

                # If the word appears more than required, move the 'left' pointer
                while seen[word] > word_count[word]:
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    left += word_len

                # If we have matched all words, add the starting index to the result
                if right - left == k:
                    res.append(left)
            else:
                # If the word is not part of the words list, reset the window
                left = right
                seen.clear()

        return res
