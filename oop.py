# 3. yield oop orqali (generatorni delegatsiya qilish)

# 1. 1 dan n gacha son generatori
class NumberGenerator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.n:
            val = self.current
            self.current += 1
            return val
        raise StopIteration

nums = NumberGenerator(5)
for x in nums:
    print(x)


# 2. Juft sonlar generatori
class EvenGenerator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            val = self.current
            self.current += 2
            return val
        raise StopIteration

evens = EvenGenerator(10)
print(list(evens))
