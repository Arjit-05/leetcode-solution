class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posi=[]
        neg=[]
        result=[]
        for num in nums:
            if num<0:
                neg.append(num)
            else:
                posi.append(num)
        
        i,j=0,0
        while i<len(posi) and j<len(neg):
            result.append(posi[i])
            result.append(neg[j])
            i+=1
            j+=1
        return result

