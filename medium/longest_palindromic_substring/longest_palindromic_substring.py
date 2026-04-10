class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        result = s[0]
        resultLength = len(result)
        
        for i in range(len(s)):
            left, right = i, i
           
           # odd palindromes
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                substring = s[left:right+1]
                substringLength = right - left + 1
               
                result = substring if substringLength > resultLength else result
                resultLength = len(result)
               
                left -= 1
                right += 1
            
            # reset left and right to check even palindromes
            left, right = i, i+1
            
            #even palindromes
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                substring = s[left:right+1]
                substringLength = right - left + 1
                
                result = substring if len(substring) > resultLength else result
                resultLength = len(result)
                
                left -= 1
                right += 1
         
        return result
        
        
                
        
        
        
   