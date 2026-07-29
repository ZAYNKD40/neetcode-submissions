class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        r= len(s)- 1
        for i in s: #if they are num and letter then compare
            if r == 0:
                break
            if not i.isalnum(): # Handle left non alphanumeric
                continue
            while not s[r].isalnum(): # handle right non alphanumeric
                r-=1
                if r == 0:
                    break
            if i.isalnum() and s[r].isalnum():
                if i.lower() == s[r].lower():
                    r-=1
                else:
                    return False
        
        return True
#for questions like this better to use while instead of for so you know when to stop instead of going
# entire string and have r==0 stopper
        