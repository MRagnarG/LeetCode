# Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        biggest = []
        word = []
        
        for char in s:
            if char in word:
                if not biggest or len(word) > biggest[1]:
                    biggest = [word.copy(), len(word)]
                
                index = word.index(char)
                word = word[index + 1 :]
            
            word.append(char)
            
        if not biggest or len(word) > biggest[1]:
            return len(word)
        
        return biggest[1]