class StackMemoryNode:
    def __init__(self, value, address):
        self.value = value
        self.address = address

class DataStructureEngine:
    @staticmethod
    def get_ds_generator(ds_type):
        if ds_type == "Stack":
            return DataStructureEngine.simulate_stack(), []
        elif ds_type == "Queue":
            return DataStructureEngine.simulate_queue(), []
        return None, []

    @staticmethod
    def simulate_stack():
        stack = []
        operations = [
            ("PUSH", 15), ("PUSH", 42), ("PUSH", 89),
            ("POP", None), ("PUSH", 33), ("POP", None)
        ]
        
        for op, val in operations:
            if op == "PUSH":
                node = StackMemoryNode(val, hex(id(val)))
                stack.append(node)
            elif op == "POP" and stack:
                stack.pop()
            
            current_snapshot = [(n.value, n.address) for n in stack]
            yield {"type": "STACK", "data": current_snapshot, "last_op": f"{op} {val if val else ''}"}

    @staticmethod
    def simulate_queue():
        queue = []
        operations = [
            ("ENQUEUE", 100), ("ENQUEUE", 200), ("ENQUEUE", 300),
            ("DEQUEUE", None), ("ENQUEUE", 400)
        ]
        
        for op, val in operations:
            if op == "ENQUEUE":
                queue.append(val)
            elif op == "DEQUEUE" and queue:
                queue.pop(0)
                
            yield {"type": "QUEUE", "data": list(queue), "last_op": f"{op} {val if val else ''}"}