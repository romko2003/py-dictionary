class Node:
    def __init__(self, key, value, hash_code):
        self.key = key
        self.value = value
        self.hash_code = hash_code


class Dictionary:
    def __init__(self, initial_capacity=8, load_factor=2 / 3):
        self.capacity = initial_capacity
        self.load_factor = load_factor
        self.threshold = int(self.capacity * self.load_factor)
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

    def __len__(self):
        return self.size

    def _hash(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        old_table = self.table
        self.capacity *= 2
        self.threshold = int(self.capacity * self.load_factor)
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_table:
            for node in bucket:
                self[node.key] = node.value

    def __setitem__(self, key, value):
        if self.size >= self.threshold:
            self._resize()

        index = self._hash(key)
        bucket = self.table[index]

        for node in bucket:
            if node.key == key:
                node.value = value
                return

        bucket.append(Node(key, value, hash(key)))
        self.size += 1

    def __getitem__(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for node in bucket:
            if node.key == key:
                return node.value

        raise KeyError(f"Key {key} not found")

    def __contains__(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        return any(node.key == key for node in bucket)
class Node:
    def __init__(self, key, value, hash_code):
        self.key = key
        self.value = value
        self.hash_code = hash_code


class Dictionary:
    def __init__(self, initial_capacity=8, load_factor=2 / 3):
        self.capacity = initial_capacity
        self.load_factor = load_factor
        self.threshold = int(self.capacity * self.load_factor)
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

    def __len__(self):
        return self.size

    def _hash(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        old_table = self.table
        self.capacity *= 2
        self.threshold = int(self.capacity * self.load_factor)
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_table:
            for node in bucket:
                self[node.key] = node.value

    def __setitem__(self, key, value):
        if self.size >= self.threshold:
            self._resize()

        index = self._hash(key)
        bucket = self.table[index]

        for node in bucket:
            if node.key == key:
                node.value = value
                return

        bucket.append(Node(key, value, hash(key)))
        self.size += 1

    def __getitem__(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for node in bucket:
            if node.key == key:
                return node.value

        raise KeyError(f"Key {key} not found")

    def __contains__(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        return any(node.key == key for node in bucket)
