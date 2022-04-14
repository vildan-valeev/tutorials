from typing import List

"""сумма ближайших двух чисел"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for k in range(len(nums)):
            for i in range(len(nums)):
                if k == i:
                    continue
                if nums[k] + nums[i] == target:
                    return [k, i]
        return list()


s = Solution()
# print(s.twoSum([2, 7, 11, 15], 9))
# print(s.twoSum([-3, 4, 3, 90], 0))
# print(s.twoSum([4, -3, 3, 90], 0))
# print(s.twoSum([3, 2, 3], 6))

def z(cash_remained):
    if cash_remained > 0:
        return f'На сегодня осталось {round(cash_remained, 2)} '
    answer = 'Денег нет, держись '
    return answer if cash_remained == 0 else answer + f'твой долг {cash_remained:.02f} '


print(z(-1531))
