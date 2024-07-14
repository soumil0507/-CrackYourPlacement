# Solution 1 : using Monotonic stack

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        # approach : find next greater element
        # substract the next greater - input array
        # return max diff if > 0 else 0

        n = len(prices)
        stack = []
        output = [None]*(n)
        i = n-1
        while i>=0:
            current = prices[i]
            while stack and stack[0] < current:
                stack.pop()
            
            if not stack:
                output[i] = -1
            
            else:
                output[i] = stack[0]
            
            stack.append(current)

            i-=1
        
        diff = []
        i = 0
        while i < n:
            diff.append(output[i] - prices[i])
            i+=1
        
        return max(diff) if max(diff) > 0 else 0
    


#Solution 2 : 2 pointer

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Approach 2 pointer

        # L = 0, R = 1
        # if L > R:
        #     L++
        #     R++
        # else:
        #     R++
        #     update max profit

        n = len(prices)
        mp = 0
        l, r = 0, 1
        while r < n:
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                mp = max(mp, profit)
            else:
                l = r
            r+=1
        
        return mp


