import abc

class Aggregate(abc.ABC):

    @abc.abstractmethod
    def iterator(self):
        pass


class Iterator(abc.ABC):
    def __init__(self, collection, cursor):
        self._collection = collection
        self._cursor = cursor

    @abc.abstractmethod
    def first(self):
        pass

    @abc.abstractmethod
    def next(self):
        pass

    @abc.abstractmethod
    def current(self):
        pass

class ListIterator(Iterator):
    def __init__(self, collection, cursor):
        super().__init__(collection, cursor)

    def first(self):
        self._cursor = -1

    def next(self):
        if self._cursor + 1 >= len(self._collection):
            self._cursor = -1
        self._cursor += 1

    def current(self):
        return self._collection[self._cursor]

class ListCollection(Aggregate):
    def __init__(self, collection):
        self._collection = list(collection)

    def iterator(self):
        return ListIterator(self._collection, -1)

#aggregate = ListCollection(CУДА СУЕМ ОБЬЕКТ ИТЕРАТОР)
#itr = aggregate.iterator(ОБЬЕКТ АГРЕГАТА)

# while True: пример
#     try:
#         itr.next()
#     except StopIteration:
#         break
#     print(itr.current())