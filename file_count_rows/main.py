# -*- coding: utf-8 -*-
import time

OUT_FILE = "done.csv"
IN_FILE = "SMM.txt"

def read_txt():
    """Read txt file - all lines"""
    with open(IN_FILE, 'r', encoding="utf-8", errors='ignore') as f:
        data_list: dict = {}
        for row in f.readlines():
            # print()
            # убираем переносы строки, убираем двоеточие, делим строку по словам в список по запятым
            list_row = row.replace("\n", "").replace(":", ",").split(",")
            # проходим по словам
            for word in list_row:
                # пропускаем , если цифры
                # TODO: добавить другие условия
                if word.isdigit():
                    continue
                # проверяем есть ли в словаре ключ, добавляем цифру или создаем новый ключ со значением 1
                if f"#{word}" in data_list:
                    data_list[f"#{word}"] += 1
                else:
                    data_list[f"#{word}"] = 1
        return data_list


def save_to_csv(data: dict):
    """Save all data to csv"""
    rows = [f"{k};{v}\n" for k, v in data.items()]
    with open(OUT_FILE, "w") as f:
        f.writelines(rows)


if __name__ == '__main__':
    t0 = time.time()

    rows = read_txt()
    save_to_csv(rows)

    tdelta = time.time() - t0
    print(tdelta)  #  1,8 с

# ------------------VERSION BY CHUNKS----------------------------------------------
# import time
# from itertools import islice
# from typing import List
#
# import pandas as pd
#
# oup_file = "don.csv"
# in_file = "s.txt"
# chunk_rows = 500


# def read_in_chunks(iter_object, chunk_size=chunk_rows):
#     """Lazy function (generator) to read a file piece by piece.
#     Default chunk size: 500."""
#     while True:
#         chunk = [row for row in islice(iter_object, chunk_size)]
#         if not chunk:
#             break
#         yield chunk
#
#
# def read_txt():
#     """Read txt file by chunks"""
#     with open(in_file, 'r', encoding="utf-8", errors='ignore') as f:
#         for slice in read_in_chunks(f):
#             # print()
#             print("next chunk")
#             data_chunk_list = []
#             for i in slice:
#                 # убираем переносы строки, убираем двоеточие, делим строку по словам в список по запятым
#                 list_row = i.replace("\n", "").replace(":", ",").split(",")
#                 # print(list_row)
#                 data_chunk_list += list_row
#             # отправляем список на сохранение в таблицу
#             save_to_csv(data_chunk_list)
#             # time.sleep(10)
#
#
# def save_to_csv(data: list):
#     """Save data to csv by Pandas"""
#     # открываем файл в датафрейм
#     # TODO: создать пустой csv если его нет...
#     df_file = pd.read_csv(oup_file, delimiter=";", header=None)
#     # очищаем список слов от чисел и вставляем хештег
#     clear_data_list = [f"#{i}" for i in data if not i.isdigit()]
#     # создаем новый датафрейм по списку
#     df_from_chunk = pd.DataFrame(list(zip(clear_data_list, [1] * len(clear_data_list))))
#     # объединяем два датафрейма с суммированием
#     concatenated_df = pd.concat([df_file, df_from_chunk]).groupby([0]).sum().reset_index()
#     # print(concatenated_df)
#     concatenated_df.to_csv(oup_file, index=False, sep=";", header=None)

if __name__ == '__main__':
    read_txt()
