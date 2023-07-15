class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        modified_s = [i.lower() for i in s if i.isalnum()]
        
        def is_palindrome(s, i=0):
            if i == len(s) // 2:
                return True
            
            if s[i] != s[-1-i]:
                return False
                
            return is_palindrome(s, i=i+1)
        return is_palindrome(modified_s)