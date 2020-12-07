from typing import TypedDict, Dict, Any

person: Dict[str, str] = {'name': 'John', 'last_name': 'Conrad', 'sex': 'm'}

dict_result: Dict[str, Any] = {'world': 'hello', 'count': 5, 'comment': 'some word'}
dict_result['comment'] = 123
print(dict_result['lol'])


class WordStat(TypedDict):
    word: str
    count: int
    comment: str


dict_result: WordStat = {'world': 'hello', 'count': 5, 'comment': 'some word'}
print(dict_result['lol'])