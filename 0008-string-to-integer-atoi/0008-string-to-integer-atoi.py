class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        # Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # If string is empty after removing spaces
        if i == n:
            return 0

        # Determine sign
        sign = 1
        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            i += 1

        num = 0

        # Convert digits
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])

            # Handle overflow
            if sign == 1 and num > 2**31 - 1:
                return 2**31 - 1
            if sign == -1 and -num < -2**31:
                return -2**31

            i += 1

        return sign * num