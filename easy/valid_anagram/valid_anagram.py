class Solution:
    # another solution that saves memory but loses runtime: sorted(s) == sorted(t)
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        else:
            frequencyS, frequencyT = {}, {}
            
            for i in range(len(s)):
                frequencyS[s[i]] = 1 + frequencyS.get(s[i], 0)
                frequencyT[t[i]] = 1 + frequencyT.get(t[i], 0)
            for char in s:
                if frequencyS[char] != frequencyT.get(char, 0):
                    return False
            return True
        
     
            