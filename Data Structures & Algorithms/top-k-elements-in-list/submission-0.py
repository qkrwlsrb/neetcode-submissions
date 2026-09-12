class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import collections

# Counter 모듈과 리스트 컴프리헨션 활용
        answer = [key for key, val in                   collections.Counter(nums).most_common(k)]
        return answer
