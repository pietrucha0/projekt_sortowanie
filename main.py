import time
import random
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from quick_sort import quick_sort
from merge_sort import merge_sort
from tim_sort import tim_sort
from intro_sort import intro_sort
from python_sort import python_sort

def measure_time(sort_func, data):
    data_copy = data.copy()
    start = time.perf_counter()
    sort_func(data_copy)
    end = time.perf_counter()
    return end - start

def generate_data(size):
    data = [random.randint(0, 100000) for _ in range(size)]
    with open("liczby.txt", "w") as f:
        f.write(str(data))
    return data

def run_comparison():
    sizes = [100, 1000, 10000]
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Insertion Sort", insertion_sort),
        ("Quick Sort", quick_sort),
        ("Merge Sort", merge_sort),
        ("TimSort", tim_sort),
        ("IntroSort", intro_sort),
        ("Sort in Python", python_sort)
    ]

    header = f"{'Rozmiar':<10} | " + " | ".join([f"{name:<15}" for name, _ in algorithms])
    print("\n" + header)
    print("-" * len(header))

    for size in sizes:
        data = generate_data(size)
        row = f"{size:<10} | "
        times = []
        for name, func in algorithms:
            exec_time = measure_time(func, data)
            times.append(f"{exec_time:<15.3f}")
        print(row + " | ".join(times))

if __name__ == "__main__":
    run_comparison()