class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # heres a braindead way to do it

        # seqNums = [12,23,34,45,56,67,78,89,123,234,345,456,567,678,789,1234,2345,3456,4567,5678,6789,
        # 12345,23456,34567,45678,56789,123456,234567,345678,456789,1234567,2345678,3456789,12345678,23456789,123456789]

        # left_index = bisect_left(seqNums, low)
        # right_index = bisect_right(seqNums, high)
        # return seqNums[left_index:right_index]

        # smarter way to do it

        a = []

        for i in range(1, 10):
            num = i
            next_digit = i + 1

            while num <= high and next_digit <= 9:
                num = num * 10 + next_digit
                if low <= num <= high:
                    a.append(num)
                next_digit += 1

        a.sort()
        return a
