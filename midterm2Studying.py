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


if __name__ == "__main__":
   
   # x = 1
   # L = [1,2,3,4,5]
   # new_list = list(map(grow,L))
   # print(new_list)

        