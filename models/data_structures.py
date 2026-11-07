import random

class StackModel:
    def __init__(self):
        self.items = []
        self.addresses = []

    def push(self, val):
        self.items.append(val)
        hex_addr = f"0x{random.randint(0x1000, 0xFFFF):04X}"
        self.addresses.append(hex_addr)

    def pop(self):
        if self.items:
            self.items.pop()
            self.addresses.pop()

    def get_state(self):
        # Returns list of tuples: (value, hex_address)
        return list(zip(self.items, self.addresses))


class QueueModel:
    def __init__(self):
        self.items = []
        self.addresses = []

    def enqueue(self, val):
        self.items.append(val)
        hex_addr = f"0x{random.randint(0x1000, 0xFFFF):04X}"
        self.addresses.append(hex_addr)

    def dequeue(self):
        if self.items:
            self.items.pop(0)
            self.addresses.pop(0)

    def get_state(self):
        return list(zip(self.items, self.addresses))