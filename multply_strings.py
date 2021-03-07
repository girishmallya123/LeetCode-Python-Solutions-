
'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

Link to the problem: https://leetcode.com/problems/multiply-strings/

'''

class Solution:
    
    def convert_to_int(self, num):
        n = len(num)-1
        i = 0
        total = 0
        while i <= n:
            total += (ord(num[i]) - 48) * 10**(n-i)
            i += 1
            
        return total
    
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.convert_to_int(num1)*self.convert_to_int(num2))



#to test locally, uncomment the below line
'''
if __name__ == "__main__":
    s = Solution()
    s.multiply("123", "456")
'''