# -----------mro ------------------
# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# class C:
#     pass
#
#
# class D(C):
#     pass
#
#
# class E(B, D):
#     pass
#
#
# def print_mro(T):
#     print(*[c.__name__ for c in T.mro()], sep=' -> ')
#
# print_mro(E)

# -----------------------
"""
У него есть ровно один метод log, который позволяет выводить в лог (в данном случае в stdout) какое-то сообщение,
добавляя при этом текущее время.
Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом, чтобы при добавлении элемента
в список посредством метода append в лог отправлялось сообщение, состоящее из только что добавленного элемента.

Примечание
Ваша программа не должна содержать класс Loggable. При проверке вашей программе будет доступен этот класс, и он будет
 содержать метод log, описанный выше.

"""
import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, x) -> None:
        super(LoggableList, self).append(x)
        self.log(x)


a = LoggableList()
a.append('msg 1')
a.append('msg 2')
print(a)
