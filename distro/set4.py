class Set:
    def __init__(self, collection):
        self.n_buckets = 1000
        self.items = [[] for i in range(self.n_buckets)]
        for item in collection:
            self.add(item)

    def __str__(self):
        items = list(self)
        return "{" + ", ".join(str(item) for item in items) + "}"

    def __contains__(self, item):
        return item in self.items[self._index(item)]

    def __iter__(self):
        return iter([item for bucket in self.items for item in bucket])

    def _index(self, item):
        return hash(item) % self.n_buckets

    def add(self, item):
        index = self._index(item)

        if item not in self.items[index]:
            self.items[index].append(item)

    def remove(self, item):
        index = self._index(item)

        try:
            self.items[index].remove(item)
        except ValueError:
            raise KeyError(item)

s = Set([1,2,3])
for item in s:
    print(item)
print(s)