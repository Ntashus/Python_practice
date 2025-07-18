Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.


class Solution(object):
    def addBinary(self, a, b):
        a = a[::-1]
        b = b[::-1]

        carry = 0 
        i = 0 
        result = []
        while i < len(a) or i < len(b) or carry:
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0

            total = digit_a + digit_b + carry

            carry = total // 2
            digit = total % 2 

            result.append(str(digit))

            i += 1


        return "".join(result[::-1])


# Accepted 296 / 296 testcases passed