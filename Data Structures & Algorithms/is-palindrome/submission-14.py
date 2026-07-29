class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        r= len(s)- 1
        for i in s: #if they are num and letter then compare
            if r == 0:
                break
            while not s[r].isalnum():
                r-=1
                if r == 0:
                    break
            if i.isalnum() and s[r].isalnum():
                if i.lower() == s[r].lower():
                    r-=1
                else:
                    return False
        
        return True

        