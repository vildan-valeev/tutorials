z = "dfdfg \rsdfsf   \n sdfsdf dsff    dsfs"


import re

mystr = " balabla\n zzz \r"

x = re.sub("^\s+|\n|\r|\s+$", '', mystr)

print(x)
import string
print(z.translate({ord(c): None for c in string.whitespace}))

