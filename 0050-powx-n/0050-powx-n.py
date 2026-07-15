class Solution:
    def myPow(self, x: float, n: int) -> float:
        binform=n
        ans=1

        if n<0:
            x=1/x
            binform=-binform

        while binform>0:
            if binform%2==1:
                ans*=x
            x*=x
            binform//=2
        return ans


            
