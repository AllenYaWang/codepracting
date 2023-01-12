from typing import List


class RentingSystem:
    def __init__(self):
        self.rentsystem = dict()

    def add_room(self, id: int, area: int, price: int, rooms: int, address: List[int]) -> bool:
        if id not in self.rentsystem:
            self.rentsystem[id] = [area, price, rooms, address]
            return True
        self.rentsystem[id] = [area, price, rooms, address]
        return False

    def delete_room(self, id: int) -> bool:
        if id in self.rentsystem:
            del self.rentsystem[id]
            return True
        return False

    def query_room(self, area: int, price: int, rooms: int, address:List[int], order_by: List[List[int]]) -> List[int]:
        res = []
        for idinfo in self.rentsystem:
            valueinfo = self.rentsystem[idinfo]
            if valueinfo[0] >= area and valueinfo[1] <= price and valueinfo[2] == rooms:
                manha = abs(valueinfo[3][0] - address[0]) + abs(valueinfo[3][1] - address[1])
                res.append([idinfo, valueinfo[0], valueinfo[1], manha])
        order_by.append([0, 1])
        res.sort(key= lambda x: [i[1] * x[i[0]] for i in order_by])  # 该函数的编写，尤其比较处甚是精彩
        return [x[0] for x in res]

if __name__ == '__main__':
    rents = RentingSystem()
    print(rents.add_room(3, 24, 200, 2, [0, 1]))
    print(rents.add_room(1, 10, 400, 2, [1, 0]))
    print(rents.query_room(1, 400, 2, [1, 1], [[3, 1], [2, -1]]))
    print(rents.delete_room(3))









