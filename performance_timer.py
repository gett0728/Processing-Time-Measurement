import time

def getPerformanceTime(func, *args, **kwargs):
    # Measure the processing time of the function.
    start = time.perf_counter()
    func(*args, **kwargs) 
    end = time.perf_counter()
    elapsed_time = end - start

    print(f"一つ目の関数の処理時間: {elapsed_time:.7f} 秒") 


def getPerformanceRelativeTime(func1, func2, *args, **kwargs):
    # Measure the processing time of the first function.
    start = time.perf_counter()
    func1(*args, **kwargs) 
    end = time.perf_counter()
    elapsed_time1 = end - start

    # Measure the processing time of the second function.
    start = time.perf_counter()
    func2(*args, **kwargs) 
    end = time.perf_counter()
    elapsed_time2 = end - start
    
    print(f"一つ目の関数の処理時間: {elapsed_time1:.7f} 秒")  
    print(f"二つ目の関数の処理時間: {elapsed_time2:.7f} 秒") 
    print(f"相対係数(一つ目の関数基準): {elapsed_time2 / elapsed_time1:.3f}") 