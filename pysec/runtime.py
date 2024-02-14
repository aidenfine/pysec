import timeit
def runtime():
    start = start_runtime()
    end = end_runtime()
    return end - start

def start_runtime():
    return timeit.default_timer()

def end_runtime():
    return timeit.default_timer()

