class MyHashMap:

    def __init__(self):
        self.key=[]
        self.val=[]

    def put(self, key: int, value: int) -> None:
        if key in self.key:
            self.val[self.key.index(key)]=value
        else:
            self.key.append(key)
            self.val.append(value)

    def get(self, key: int) -> int:
        if key in self.key:
            return self.val[self.key.index(key)]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.key:
            loc=self.key.index(key)
            self.val.pop(loc)
            self.key.pop(loc)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)