class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        max_len = 0
        
        for i in range(s_len):
            # odd
            until = min(i, s_len-i-1) 
            for j in range(until+1):
                if s[i-j] != s[i+j]:
                    j -= 1
                    break
                    
            if max_len < 2*j+1:
                lps = [i-j, i+j+1]
                max_len = 2*j+1
                
            # even
            until = min(i+1, s_len-i-1)
            j = 0
            for j in range(1,until+1):
                if s[i-j+1] != s[i+j]:
                    j -= 1
                    break
                    
            if max_len < 2*j:
                lps = [i-j+1, i+j+1]
                max_len = 2*j
          
        return s[lps[0]:lps[1]]