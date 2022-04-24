class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = self.x * self.y

    def __add__(self, room_obj):
        if isinstance(room_obj, Room):
            return self.area + room_obj.area
        raise TypeError('Wrong object')


r1 = Room(3, 5)
r2 = Room(4, 7)
# print(r1.area, r2.area)
# print(r1 + r2)


# polymorphism - функция в зависимости от типа данных меняет свое поведение
l = [1,2,3]
d ={
    "a": 1,
    "b": 2,

}
s = "123"
print(len(l))
print(len(d))
print(len(s))

print(1 + 1)
print("1" + "1")
