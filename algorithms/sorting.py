import random

class AlgorithmEngine:
    @staticmethod
    def get_sorting_generator(algo_name, size=15):
        raw_data = [random.randint(15, 95) for _ in range(size)]
        
        if algo_name == "Bubble Sort":
            return AlgorithmEngine.bubble_sort(list(raw_data)), raw_data
        elif algo_name == "Selection Sort":
            return AlgorithmEngine.selection_sort(list(raw_data)), raw_data
        elif algo_name == "Insertion Sort":
            return AlgorithmEngine.insertion_sort(list(raw_data)), raw_data
        
        return None, raw_data

    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                yield arr, [j, j + 1]  # Active comparison
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    yield arr, [j, j + 1]  # Active swap state

    @staticmethod
    def selection_sort(arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                yield arr, [j, min_idx]
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            yield arr, [i, min_idx]

    @staticmethod
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                yield arr, [j, j + 1]
                j -= 1
            arr[j + 1] = key
            yield arr, [j + 1]