class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = [0]*26
        for char in s:
            check[ord(char)-97] += 1
        for char in t:
            if check[ord(char)-97] > 0:
                check[ord(char)-97] -= 1
            else:
                return False    
        if sum(check)>0:
            return False
        return True            
        