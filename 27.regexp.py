import re

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


text = '/send 345645766 Language: python3 ource: s = '
#
# # search = re.search(r'@(\S+)', text)
# # print(search.group(0))
#
# search = re.search(r'\b@(\S+)', text)
# print(search)
print(text.split(" ", 2)[-1])
print(text.split(" ", 2)[1])
