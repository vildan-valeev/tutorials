# -*- coding: utf-8 -*-
from itertools import islice

import pandas as pd

oup_file = "don.csv"
in_file = "SMM.txt"
chunk_rows = 500


def read_in_chunks(iter_object, chunk_size=chunk_rows):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 500."""
    while True:
        chunk = [row for row in islice(iter_object, chunk_size)]
        if not chunk:
            break
        yield chunk


def read_txt():
    """Read txt file by chunks"""
    with open(in_file, 'r', encoding="utf-8", errors='ignore') as f:
        for slice in read_in_chunks(f):
            # print()
            # print("next chunck")
            data_chunk_list = []
            for i in slice:
                # убираем переносы строки, убираем двоеточие, делим строку по словам в список по запятым
                list_row = i.replace("\n", "").replace(":", ",").split(",")
                # print(list_row)
                data_chunk_list += list_row
            # отправляем список на сохранение в таблицу
            save_to_csv(data_chunk_list)
            # time.sleep(10)


def save_to_csv(data: list):
    """Save data to csv by Pandas"""
    # открываем файл в датафрейм
    # TODO: создать пустой csv если его нет...
    df_file = pd.read_csv(oup_file, delimiter=";", header=None)
    # очищаем список слов от чисел и вставляем хештег
    clear_data_list = [f"#{i}" for i in data if not i.isdigit()]
    # создаем новый датафрейм по списку
    df_from_chunk = pd.DataFrame(list(zip(clear_data_list, [1] * len(clear_data_list))))
    # объединяем два датафрейма с суммированием
    concatenated_df = pd.concat([df_file, df_from_chunk]).groupby([0]).sum().reset_index()
    # print(concatenated_df)
    concatenated_df.to_csv(oup_file, index=False, sep=";", header=None)


if __name__ == '__main__':
    read_txt()

