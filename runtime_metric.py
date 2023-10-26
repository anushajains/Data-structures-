import time

def runtime_metric(func): #decorator take argument func
    def measurement(*args, **kwargs):
        #check start time
        start_time = time.perf_counter_ns()
        result = func(*args, **kwargs)
        #check end time
        end_time = time.perf_counter_ns()
        #subtract start time from end time to get time taken to execute
        print(f"Function {func.__name__} took {end_time - start_time} nanoseconds to execute.")
        return result
    return measurement





