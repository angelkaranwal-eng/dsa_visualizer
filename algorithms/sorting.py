# Developed by Member 3: Shubhangi Sharma (Algorithms & State Generators)

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