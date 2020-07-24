a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

x = 0
y = 2

i = 1
new_list = []
while i < 100:
    if a[x:y]:
        print(f'slice {i}', a[x:y])
        for m in a[x:y]:
            if m % 3 == 0:
                new_list.append(m)

    i += 1
    x += 2
    y += 2

print(new_list)
# new_list = []
# while i < 100:
#     if a[x:y]:
#         print(f'slice {i}', a[x:y])
#         for m in a[x:y]:
#             if m % 3 == 0:
#                 new_list.append(m)
#             else:
#                 continue
#         else:
#             continue
#     i += 1
#     x += 2
#     y += 2
