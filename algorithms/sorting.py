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
            def bubble_sort_generator(arr):
    data = list(arr)
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Yield comparing state (Active indices: j, j+1, Action: 'COMPARE')
            yield {
                'array': list(data),
                'active': [j, j + 1],
                'action': 'COMPARE'
            }
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                # Yield swapping state
                yield {
                    'array': list(data),
                    'active': [j, j + 1],
                    'action': 'SWAP'
                }
    # Final state
    yield {
        'array': list(data),
        'active': [],
        'action': 'DONE'
    }


def selection_sort_generator(arr):
    data = list(arr)
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            yield {
                'array': list(data),
                'active': [min_idx, j],
                'action': 'COMPARE'
            }
            if data[j] < data[min_idx]:
                min_idx = j
        if min_idx != i:
            data[i], data[min_idx] = data[min_idx], data[i]
            yield {
                'array': list(data),
                'active': [i, min_idx],
                'action': 'SWAP'
            }
    yield {
        'array': list(data),
        'active': [],
        'action': 'DONE'
    }


def insertion_sort_generator(arr):
    data = list(arr)
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            yield {
                'array': list(data),
                'active': [j, j + 1],
                'action': 'COMPARE'
            }
            data[j + 1] = data[j]
            j -= 1
            yield {
                'array': list(data),
                'active': [j + 1],
                'action': 'SWAP'
            }
        data[j + 1] = key
    yield {
        'array': list(data),
        'active': [],
        'action': 'DONE'
    }