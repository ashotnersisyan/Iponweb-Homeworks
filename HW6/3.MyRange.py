class MyRangeError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class MyRange:
    def __init__(self, current=0, end=1, step=1):
        if isinstance(current, int) or isinstance(current, float):
            self.__current = current
        else:
            raise MyRangeError("The startpoint should be a number", current)
        if isinstance(end, int) or isinstance(end, float):
            self.__end = end
        else:
            raise MyRangeError("The endpoint should be a number", end)
        if isinstance(step, int) or isinstance(step, float):
            self.__step = step
        else:
            raise MyRangeError("The step size should be a number", step)

    def __repr__(self):
        return repr(f"A range object starting at {self.__current}, ending at {self.__end} "
                    f"and step size of {self.__step}.")

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__end = value
        else:
            raise MyRangeError("The endpoint should be a number", value)

    @property
    def current(self):
        return self.__current

    @current.setter
    def current(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__current = value
        else:
            raise MyRangeError("The startpoint should be a number", value)

    @property
    def step(self):
        return self.__step

    @step.setter
    def step(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__step = value
        else:
            raise MyRangeError("The step size should be a number", value)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current <= self.__end:
            if self.__step < 0:
                raise StopIteration
            if self.__current < self.__end:
                current = self.__current
                self.__current += self.__step
                return current
            else:
                raise StopIteration
        else:
            if self.__step > 0:
                raise StopIteration
            if self.__current > self.__end:
                current = self.__current
                self.__current += self.__step
                return current
            else:
                raise StopIteration

    def __len__(self):
        range_len = 0
        curr = self.__current
        if self.__current <= self.__end:
            while curr < self.__end:
                range_len += 1
                curr += self.__step
            return range_len
        else:
            while curr > self.__end:
                range_len += 1
                curr += self.__step
            return range_len

    def __getitem__(self, item):
        position = 1
        curr = self.__current
        if self.__current <= self.__end:
            while position <= item:
                position += 1
                curr += self.__step
                if curr > self.__end:
                    return MyRangeError("Index out of range", item)
            return curr
        else:
            while position <= item:
                position += 1
                curr += self.__step
                if curr < self.__end:
                    return MyRangeError("Index out of range", item)
            return curr

    def __reversed__(self):
        curr = self.__current
        if self.__current <= self.__end:
            while curr < self.__end:
                curr += self.__step
        else:
            while curr > self.__end:
                curr += self.__step
        curr -= self.__step
        return MyRange(curr, self.__current-(self.__step/2), -self.__step)


range1 = MyRange(1, 10, 1)
print(range1)
print(next(range1))
print(next(range1))
# while True:
#     print(next(range1))
a = reversed(MyRange(1, 10, 1))
print(a)
print(len(a))
for i in reversed(a):
    print(i)
print(reversed(a))

