def test(s):
    return True if len(set(''.join(i for i in s if i.isalpha()).lower())) == 26 else False

    # s = 'The quick brown fox jumps over the lazy dog'
    # if len(set(''.join(i for i in s if i.isalpha()).lower())) == 26:
    #     return True
    # else:
    #     return False
print(test('The quick brown fox jumps over the lazy 56151321 dog'))
def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())

print(is_pangram('The quick brown fox jumps over the lazy 56151321 dog'))