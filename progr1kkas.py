def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        true = True
        x = str(x)
        for i in len(x):
            if x[i] == x(len(x)-i):
                true = True
            else:
                true = False
        return true

print(isPalindrome(121))