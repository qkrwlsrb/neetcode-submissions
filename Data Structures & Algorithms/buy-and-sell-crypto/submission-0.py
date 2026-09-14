class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = [0]
        for i in range(len(prices)-1):
            c = 0
            for j in range(i+1,len(prices)):
                c = max(prices[j]-prices[i],c)
            answer.append(c)
        return max(answer)