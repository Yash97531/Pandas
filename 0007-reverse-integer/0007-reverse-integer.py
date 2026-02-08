class Solution(object):
    def reverse(self, x):
        
        if(x<0):
            y = -int(str(-x)[::-1])
        else:
            y = int(str(x)[::-1])


        if(y<(-2**31)):
            return 0
        elif(y>((2**31)-1)):
            return 0
        else:
            return y
obj = Solution()
obj.reverse(123)   
