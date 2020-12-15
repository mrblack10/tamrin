class Counter:  # hamon class range
    def __init__(self, Start, Stop, Step=1):
        self.start = Start
        self.stop = Stop
        self.step = Step
        self.current = Start

    def __iter__(self):
        return self

    def __next__(self):

        if (self.current < self.stop and self.step > 0) \
                or (self.current > self.stop and self.step < 0):
            num = self.current
            self.current += self.step
            return num
        else:
            raise StopIteration

    def __len__(self):
        return self.stop - self.start

    def __repr__(self):
        if self.step == 1:
            st = f"Counter({self.start}, {self.stop})"
        else:
            st = f"Counter({self.start}, {self.stop}, {self.step})"

        return st


mycounter_1 = Counter(2, 10)
mycounter_2 = Counter(10,2,-3)
for num in mycounter_2:
    print(num,end = "\t")
# print(len(mycounter))
# print(mycounter)
# a = range(20, 2, -1)
# print(list(a))