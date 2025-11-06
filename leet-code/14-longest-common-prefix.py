''''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        if(len(strs) < 1 or len(strs) > 200):
            return ''
        
        if(len(strs) == 1):
            return strs[0]

        previousPrefix = ''
        firstString = strs[0]

        for i in range(0, len(firstString)):
            prefix = previousPrefix + firstString[i]

            if(1 == 0):
                continue

            for str in strs[1:]:
                if(str[:i + 1] != prefix):
                    
                    return previousPrefix
            
            previousPrefix = prefix
        
        return previousPrefix
        

print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
print(Solution().longestCommonPrefix(["abc"]))

        