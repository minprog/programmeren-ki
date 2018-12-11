class Set:
    def __init__(self, collection):
        self.items = list(collection)

    def __str__(self):
        return "{" + ", ".join(str(item) for item in self.items) + "}"

    def __contains__(self, item):
        return item in self.items

    def add(self, item):
        if item not in self.items:
            self.items.append(4)

s = Set([1,2,3])
print(s)
s.add(4)
print(s)
print(5 in s)

s = Set(range(10000))
for i in range(100000):
    i in s