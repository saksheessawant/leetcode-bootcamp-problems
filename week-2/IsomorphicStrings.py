class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        s_to_t = {}
        t_to_s = {}
    
        for i in range(len(s)):
            if s[i] in s_to_t:
                if s_to_t[s[i]] != t[i]:
                    return False
            else:
                if t[i] in t_to_s:
                    return False
                s_to_t[s[i]] = t[i]
                t_to_s[t[i]] = s[i]
    
        return True
