"""Integer-key hash table using universal hashing and separate chaining."""
import random


class ChainedHashTable:
    """A dynamic chained dictionary for integer keys (bool excluded)."""

    PRIME = 2_305_843_009_213_693_951  # 2**61 - 1

    def __init__(self, capacity=8, seed=None):
        if not isinstance(capacity, int) or isinstance(capacity, bool) or capacity < 1:
            raise ValueError('capacity must be a positive integer')
        self._minimum = max(4, capacity)
        self._buckets = [[] for _ in range(self._minimum)]
        self._size = 0
        rng = random.Random(seed)
        self._a = rng.randrange(1, self.PRIME)
        self._b = rng.randrange(self.PRIME)

    def _index(self, key):
        if not isinstance(key, int) or isinstance(key, bool):
            raise TypeError('keys must be integers (not bool)')
        return ((self._a * (key % self.PRIME) + self._b) % self.PRIME) % len(self._buckets)

    def _resize(self, capacity):
        old = self._buckets
        self._buckets = [[] for _ in range(capacity)]
        for bucket in old:
            for key, value in bucket:
                self._buckets[self._index(key)].append((key, value))

    def insert(self, key, value):
        index = self._index(key)
        bucket = self._buckets[index]
        for i, (existing, _) in enumerate(bucket):
            if existing == key:
                bucket[i] = (key, value)
                return
        if (self._size + 1) / len(self._buckets) > 0.75:
            self._resize(len(self._buckets) * 2)
            index = self._index(key)
        self._buckets[index].append((key, value))
        self._size += 1

    def search(self, key):
        for existing, value in self._buckets[self._index(key)]:
            if existing == key:
                return value
        raise KeyError(key)

    def delete(self, key):
        bucket = self._buckets[self._index(key)]
        for i, (existing, value) in enumerate(bucket):
            if existing == key:
                bucket.pop(i)
                self._size -= 1
                if len(self._buckets) > self._minimum and self.load_factor < 0.20:
                    self._resize(max(self._minimum, len(self._buckets) // 2))
                return value
        raise KeyError(key)

    @property
    def load_factor(self):
        return self._size / len(self._buckets)

    def __len__(self):
        return self._size

    @property
    def capacity(self):
        return len(self._buckets)
