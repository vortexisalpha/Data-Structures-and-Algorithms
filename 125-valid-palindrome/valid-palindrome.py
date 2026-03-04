alpha = {"a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4","5", "6", "7", "8", "9"}

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = [c for c in s if c in alpha]
        l_ptr = 0
        r_ptr = len(new_s)-1
        while l_ptr <= r_ptr:
            if new_s[l_ptr] != new_s[r_ptr]:
                return False
            l_ptr+=1
            r_ptr-=1
        return True