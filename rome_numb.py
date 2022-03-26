nums = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "G": 5000,
    "H": 10000
}


def rome_numb(s):
    result = 0
    for i, c in enumerate(s):
        if i + 1 < len(s) and nums[s[i]] < nums[s[i + 1]]:
            result -= nums[s[i]]
        else:
            result += nums[s[i]]
    return result


def numb_rome(num):
    # inv_nums = {
    #     1: "I",
    #     5: "V",
    #     ...
    # }
    inv_nums = {v: k for k, v in nums.items()}

    print([i for i in inv_nums])
    string_num = str(num)
    result = ''
    for i, s in enumerate(string_num):

        r: str = '0' * len(string_num[i + 1:])  # рядность

        # if int(s + r) in inv_nums:  # совпадения - отбираем пятерки и единицы
        #     result += inv_nums[int(s + r)]
        if int(s) == 4:
            result += (inv_nums[int('1' + r)] + inv_nums[int('5' + r)])
        elif int(s) == 9:
            result += (inv_nums[int('1' + r)] + inv_nums[int('1' + r + '0')])
        elif 0 <= int(s) < 4:  # здесь точно не будет 5 и 1
            result += inv_nums[int('1' + r)] * int(s)
        else:  # 6 - 8
            # print(s)
            # print(inv_nums[int('5' + r)], inv_nums[int('1' + r)]*(int(s) - 5))
            result += (inv_nums[int('5' + r)] + inv_nums[int('1' + r)] * (int(s) - 5))

    return result


# print(rome_numb('CCCXL'))
# print(numb_rome(3549))
# print(numb_rome(2008))

class TEST:
    n = 12
    @staticmethod
    def from_(dd):
        print(__class__.__dict__.get("n"))
        print(__class__.__getattribute__('n'))

        # print(dd, n)

TEST.from_(55)
