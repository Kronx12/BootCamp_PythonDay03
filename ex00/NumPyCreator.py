import numpy
import random


class NumPyCreator:
    def from_list(self, lst, dtype=int):
        return numpy.array(lst, dtype)

    def from_tuple(self, tpl, dtype=int):
        return numpy.array(tpl, dtype)

    def from_iterable(self, itr, dtype=int):
        return numpy.array(itr, dtype)

    def from_shape(self, shape, value=0, dtype=int):
        return numpy.array([[value] * shape[1]] * shape[0], dtype)

    def random(self, shape, dtype=int):
        return numpy.random.rand(shape[0], shape[1])

    def identity(self, n, dtype=int):
        return numpy.identity(n, dtype)


if __name__=="__main__":
    npc = NumPyCreator()
    print(npc.from_list([[1,2,3], [4,5,6], [7,8,9]], float))
    print(npc.from_list(("a", "b", "c"), str))
    print(npc.from_list(range(5), float))

    shape = (3, 5)
    print(npc.from_shape(shape, dtype=float))
    shape = (3, 5)
    print(npc.from_shape(shape, 1, dtype=float))

    shape = (3, 5)
    print(npc.random(shape))

    print(npc.identity(4, float))
