import re
import random
# text = '123'\
#        '+79261234567'\
#        '+89261234567'\
#        '+77271212888'\
#        '+9271255512'\
#        '8 927 123 8 123'
#
#
# tel = r"^\+79\d{9}(?=\s|$)"
#
# result = re.fullmatch(tel, text)
# print(result)


# text = '/send 345645766 Language: python3 ource: s = '
#
# # search = re.search(r'@(\S+)', text)
# # print(search.group(0))
#
# search = re.search(r'\b@(\S+)', text)
# print(search)
# print(text.split(" ", 2)[-1])
# print(text.split(" ", 2)[1])
import time

"""
(?<!\d) - сразу слева не должно быть цифры
(?:0?[1-9]|[12][0-9]|3[01]) - целые числа от 1 до 31 (перед числами от 1 до 9 может быть необязательный 0)
- - дефис
(?:0?[1-9]|1[0-2]) - целые числа от 1 до 12 (перед числами от 1 до 9 может быть необязательный 0)
- - дефис
(?:19[0-9][0-9]|20[01][0-9]) - целые числа от 1900 до 2019
(?!\d) - сразу справа не должно быть цифры

"""
# TODO: проверка на другие символы вместо точек -> ( \. )
pattern = r'(?<!\d)(?:0[1-9]|[12][0-9]|3[01])\.(?:0[1-9]|1[0-2])\.(?:20[02][0-9]) (?:0[0-9]|1[0-9]|2[0-4])\:(?:0[0-9]|[012345][0-9])(?!\d)'


def test(s, p):
    result = re.fullmatch(pattern=p, string=s)
    if result:
        print(s, 'yes')
    else:
        print(s, 'no')


def result():
    dd = "{:02d}".format(random.randint(1, 31))
    mm = "{:02d}".format(random.randint(1, 12))
    yy = random.randint(2020, 2029)
    h = "{:02d}".format(random.randint(0, 23))
    m = "{:02d}".format(random.randint(0, 59))
    return f'{dd}.{mm}.{yy} {h}:{m}'



# while True:
#     time.sleep(0.5)
#     test(result(), pattern)



