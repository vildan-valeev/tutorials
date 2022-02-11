import pathlib

from typing import List, Optional, Tuple

candidates = [
    {"name": "Vasya", "scores": {"math": 20, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya", "scores": {"math": 92, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
    {"name": "Vasya2", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya2", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya2", "scores": {"math": 92, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
    {"name": "Vasya3", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya3", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},

    {"name": "Vasya6", "scores": {"math": 60, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya6", "scores": {"math": 44, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya4", "scores": {"math": 92, "russian_language": 37, "computer_science": 30}, "extra_scores": 1},
    {"name": "Vasya7", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya7", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya7", "scores": {"math": 90, "russian_language": 37, "computer_science": 34}, "extra_scores": 1},
    {"name": "Vasya8", "scores": {"math": 52, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya8", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya8", "scores": {"math": 91, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
    {"name": "Petya6", "scores": {"math": 92, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
    {"name": "Vasya4", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya4", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya3", "scores": {"math": 90, "russian_language": 35, "computer_science": 34}, "extra_scores": 1},
    {"name": "Vasya5", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya5", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya5", "scores": {"math": 94, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
]


def find_top_20(candidates_list: List[dict]) -> List[dict]:
    """ТОП-20: сортировка"""

    def full_score(i):
        """сумма всех баллов"""
        return i['scores']['math'] + i['scores']['russian_language'] + i['scores']['computer_science'] + i[
            'extra_scores']

    def last_chance(i):
        """баллы информатика и математика"""
        return i['scores']['math'] + i['scores']['computer_science']

    # сортируем топ 19
    sorted_candidates = sorted(candidates_list, key=full_score, reverse=True)
    # проверяем крайнего кандидата
    if full_score(sorted_candidates[19]) == full_score(sorted_candidates[20]):
        sorted_candidates[19] = sorted(sorted_candidates[20:22],
                                       key=last_chance,
                                       reverse=True)[0]  # добавляем последнего кандидата
    return sorted_candidates[:20]


# find_top_20(candidates)


names = ["Vasya", "Alice", "Petya", "Jenny", "Fedya", "Viola", "Mark", "Chris", "Margo"]
birthday_years = [1992, 1995, 2000, None, None, None, None, 1998, 2001]
genders = ["Male", "Female", "Male", "Female", "Male", None, None, None, None]


def get_inductees(names_: List[str], birthday_years_: List[Optional[int]], genders_: List[Optional[str]]) -> Tuple[
    List[str], List[str]]:
    """Собираем военнообязанных в армию - за ордууууууу))))"""

    female = 'Female'
    # приводим к list of dict для сортировки (отсортирован по non-female)
    students = [{'name': n, 'b_year': b, 'gen': g} for n, b, g in zip(names_, birthday_years_, genders_) if g != female]
    inductees = []
    unidentified = []
    other = []
    # import datetime  # move to top
    # year_now = datetime.datetime.now().year  # для 2022 года
    for i in students:
        if i['b_year'] is None:  # без даты рождения всех в unidentified
            unidentified.append(i['name'])
        # elif 18 <= year_now - i['b_year'] < 30:
        elif 18 <= 2021 - i['b_year'] < 30:
            if i['gen'] is not None:  # кто от 18 и до 30 с гендером Male - в inductees,
                inductees.append(i['name'])
            else:  # остальные в unidentified - без гендера но подходят по дате
                unidentified.append(i['name'])
        else:  # все остальные - c датой и Male, но не подходят по возрасту
            other.append(i['name'])
    return inductees, unidentified


# print(get_inductees(names, birthday_years, genders))


know_english = ["Vasya", "Jimmy", "Max", "Peter", "Eric", "Zoi", "Felix"]
sportsmen = ["Don", "Peter", "Eric", "Jimmy", "Mark"]
more_than_20_years = ["Peter", "Julie", "Jimmy", "Mark", "Max"]


def find_athlets(*args: List[str]) -> set:
    """ Определяем список совпадений.
        Количество совпадений имен в счетчике должна быть равна(или больше) количеству аргументов функции(списков)
        это будет значить что имя есть во всех списках.
    """
    return set.intersection(*[set(i) for i in args])


# print(find_athlets(know_english, sportsmen, more_than_20_years))


# import collections
# c = collections.Counter()
# for word in ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']:
#     c[word] += 1
# print(c)


students_avg_scores = {'Max': 4.964,
                       'Eric': 4.962,
                       'Peter': 4.923,
                       'Mark': 4.957,
                       'Julie': 4.95,
                       'Jimmy': 4.973,
                       'Felix': 4.937,
                       'Vasya': 4.911,
                       'Don': 4.936,
                       'Zoi': 4.937}


def make_report_about_top3(students: dict) -> pathlib.Path.name:
    """ save top-3"""
    import csv  # move to top
    from pathlib import Path  # move to top
    file_name = 'output.xlsx'
    # with open('output.csv', 'w+') as output:
    # windows-ом не пользуюсь, поэтому не могу сказать насколько это правильно...
    with open(file_name, 'w+') as output:
        writer = csv.writer(output)
        # print(dict(sorted(students.items(), key=lambda item: item[1], reverse=True)[:3]))
        for key, value in dict(sorted(students.items(), key=lambda item: item[1], reverse=True)[:3]).items():
            writer.writerow([key, value])

    return Path(file_name).absolute().name


contacts = {
    'name': 'Вильдан',
    'phone': 89279388882,
    'e-mail': 'vildan.maydanovich.valeev@gmial.com',
    'tg': '@vildan_valeev',

}

# make_report_about_top3(students_avg_scores)

