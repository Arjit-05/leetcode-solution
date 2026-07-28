class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        for ch in s:
            if ch.isalnum():
                ans+=ch.lower()

        if ans== ans[::-1]:
            return True
        return False

        

