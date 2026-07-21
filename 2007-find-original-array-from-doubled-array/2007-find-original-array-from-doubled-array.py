class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2!=0:
            return []

        changed.sort()

        freq={}
        for num in changed:
            freq[num]=freq.get(num,0)+1
        original=[]

        for num in changed:
            if freq[num]==0:
                continue
            
            if freq.get(2*num,0)==0:
                return []
            original.append(num)

            freq[num]-=1
            freq[2*num]-=1
        return original

            
