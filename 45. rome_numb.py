num= {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

def rome_numb(s):
    result = 0
    for i, c in enumerate(s):
        if i + 1 < len(c) and num[s[i]] < num[s[i+1]]:
            result -= num[s[i]]
        else:
            result += num[s[i]]
    return result

print(rome_numb('XV'))