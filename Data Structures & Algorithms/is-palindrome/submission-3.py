class Solution:
    def isPalindrome(self, s: str) -> bool:
        #extract, join and check one by one
        forward, backward = "",""
        for i in range(len(s)):
            if s[i].isalnum():
                forward += s[i].lower()
        
        #find backward
        for i in range(len(s)-1,-1,-1):
            if s[i].isalnum():
                backward += s[i].lower()
        
        return forward == backward

