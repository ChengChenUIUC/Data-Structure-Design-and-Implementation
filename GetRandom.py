class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()
        self.arr = []
        self.n = 0
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            return False
        self.d[val] = self.n
        self.arr.append(val)
        self.n += 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            return False
        else:
            #print self.arr,self.d,self.n, val
            temp = self.d[val]
            self.n -= 1
            self.arr[self.n], self.arr[temp] = self.arr[temp], self.arr[self.n]
            self.d[self.arr[temp]] = temp
            self.d.pop(val)
            self.arr.pop(self.n)
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.n != 0:
            return random.choice(self.arr)


# RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()