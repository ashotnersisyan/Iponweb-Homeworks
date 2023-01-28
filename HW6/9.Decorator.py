def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        return func(*args, **kwargs)
    wrapper.counter = 0
    return wrapper


@call_counter
def base():
    pass


for i in range(10):
    base()
    print(base.counter)