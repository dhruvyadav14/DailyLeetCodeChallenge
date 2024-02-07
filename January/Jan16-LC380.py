import random


class RandomizedSet:

    def __init__(self):
        self.stack = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.stack)
        self.stack.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.map:
            lastElement = self.stack[-1]
            index = self.map[val]

            self.map[lastElement] = index
            self.stack.pop()
            if index < len(self.stack):
                self.stack[index] = lastElement
            self.map.pop(val)
            return True

        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.stack)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()