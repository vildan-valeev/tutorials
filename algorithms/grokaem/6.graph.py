from collections import deque


graph = {
    'you': ['alice', 'bob', 'claire'],
    'bob': ['anuj', 'peggy'],
    'alice': ['peggy'],
    'claire': ['thom', 'jonny'],
    'anuj': [],
    'peggy': [],
    'thom': [],
    'jonny': []
}


def person_is_seller(name):
    return name[-1] == 'm'

print(graph)
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    # Этот массив используется дпя отслеживания уже проверенных людей
    print(search_queue)
    searched = []
    while search_queue:
        person = search_queue.popleft()
        # Человек проверяется только в том случае, если он не проверялся ранее
        print(person)
        if not person in searched:
            if person_is_seller(person):
                print(person + " is а mango seller!")
                return True

            else:  # Человек помечается как уже проверенный

                search_queue += graph[person]
                searched.append(person)

    return False


search("you")
