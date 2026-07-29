class Solution:
    def isPalindrome(self, s: str) -> bool:
        scontainer = ''
        for i in s:
            if i.isalnum():
                scontainer += i.lower()
        print(scontainer, scontainer[::-1])
        return scontainer == scontainer[::-1]
        