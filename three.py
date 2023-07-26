#first solution
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        elif n==1:
            return True
        elif n%3==0:
            return True
        else:
            return False
#second solution
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and 3**19%n==0
