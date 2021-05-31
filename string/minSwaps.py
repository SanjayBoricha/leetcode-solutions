class Solution:
    def minSwaps(self, s: str) -> int:  
        zeros = 0
        ones = 0
        for i in range(len(s)):
            if(s[i] == "1"):
                ones += 1
            else:
                zeros += 1

        if(abs(zeros - ones) >= 2):
            return -1

        # counts number of zeroes at odd 
        # and even positions 
        odd_0, even_0 = 0, 0
    
        # counts number of ones at odd 
        # and even positions 
        odd_1, even_1 = 0, 0
    
        for i in range(len(s)) :
    
            if i % 2 == 0 :
    
                if s[i] == "1" :
                    even_1 += 1
                else :
                    even_0 += 1
                    
            else :
                if s[i] == "1" :
                    odd_1 += 1
                else :
                    odd_0 += 1
    
        # alternating string starts with 0 
        cnt_swaps_1 = min(even_0, odd_1)
    
        # alternating string starts with 1 
        cnt_swaps_2 = min(even_1, odd_0)
    
        # calculates the minimum number of swaps 
        return min(cnt_swaps_1, cnt_swaps_2)


print(Solution().minSwaps('100'))