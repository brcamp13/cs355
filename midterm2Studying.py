
from functools import reduce
import random

x = 0
def add(a):
    global x
    x = a+x
    return x


def grow (c):
    return x+c


def outer (f):
    def inner (g, y):
        return f(y)+g(y)
        return inner

class Evens(object):
        def __init__(self):
                self.current = 2
        
        def __next__(self): 
                result = self.current
                self.current += 2
                return result

        def __iter__(self): 
                return self


class Stream(object): 
        def __init__(self, first, compute_rest, empty = False):
                self.first = first
                self._compute_rest = compute_rest
                self.empty = empty
                self._rest = None
                self._computed = False

        @property
        def rest(self): 
                assert not self.empty, 'Empty streams have no rest'
                if not self._computed: 
                        self._rest = self._compute_rest()
                        self._computed = True
                return self._rest

# Stream of random numbers within min and max and starting at k 
def streamRandoms(k, minimum, maximum):

    def compute_rest():
        return streamRandoms(random.randint(minimum, maximum), minimum, maximum)

    return Stream(k, compute_rest)


if __name__ == "__main__":
   
   # evenNums = Evens()
   # n = 10
   # while n > 0: 
           # item = evenNums.__next__()
           # print(item)
           # n -= 1
           
        rStream = streamRandoms(1,1,100)
        myList = []
        for i in range(0,10):
                myList.append(rStream.first)
                rStream = rStream.rest
        
        print(myList)
        
        

        