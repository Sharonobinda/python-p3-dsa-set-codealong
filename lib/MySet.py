class MySet:
    def __init__(self, elements=None):
        self.dictionary = {}
        if elements is not None:
            for element in elements:
                self.dictionary[element] = True

    def __repr__(self):
        return f"MySet({list(self.dictionary.keys())})"

    def add(self, element):
        self.dictionary[element] = True

    def delete(self, element):
        if element in self.dictionary:
            del self.dictionary[element]

    def has(self, element):
        return element in self.dictionary

    def size(self):
        return len(self.dictionary)

    def union(self, other_set):
        new_set = MySet(self.dictionary.keys())
        for element in other_set.dictionary.keys():
            new_set.add(element)
        return new_set

    def intersection(self, other_set):
        new_set = MySet()
        for element in self.dictionary.keys():
            if element in other_set.dictionary:
                new_set.add(element)
        return new_set

    def difference(self, other_set):
        new_set = MySet()
        for element in self.dictionary.keys():
            if element not in other_set.dictionary:
                new_set.add(element)
        return new_set

    def is_subset(self, other_set):
        for element in self.dictionary.keys():
            if element not in other_set.dictionary:
                return False
        return True
