v = [1, 4, 4, 4, 5, 6, 30, 7]

# z = v.__iter__()
# print(z._)
# print(z.__next__())
# print(z.__next__())
# print(z.__next__())
def get_loop_item(my_list, item, spacing):
    if isinstance(spacing, int):
        return my_list[(my_list.index(item) + spacing) % len(my_list)]
    elif isinstance(spacing, list):
        return [get_loop_item(my_list, item, space) for space in spacing]
    return None

print([get_loop_item(my_list, item, space) for space in [-1, 1]])
print(get_loop_item(v, 5, 1))


# tmp = []
# lst = [(1243, 517), (1313, 540), (1313, 541), (1161, 558), (1383, 576), (1384, 576), (1219, 587), (1220, 587),
#      (1453, 611), (1454, 611)]
# f = []
# s = []
# tmp = []
# for i in lst:
#     # print(i)
#     if i[0] not in f:
#         f.append(i[0])
#         tmp.append(i)
# # print(tmp)
# print(f)
# result = []
# for i in tmp:
#     # print(i)
#     if i[1] not in s:
#         s.append(i[1])
#         result.append(i)
#     # print()
# print(result)


spisok = [(1243, 517), (1313, 540), (1313, 541), (1161, 558), (1383, 576), (1384, 576), (1219, 587), (1220, 587),
          (1453, 611), (1454, 611)]

nov = [spisok[0], ]
for i in range(len(spisok)):
    for a in range(len(spisok)):
        if spisok[i] == spisok[a]:
            continue
        if ((abs(spisok[i][0] - spisok[a][0])) < 4) and ((abs(spisok[i][1] - spisok[a][1])) < 4):
            if spisok[i] not in nov:
                nov.append(spisok[a])

