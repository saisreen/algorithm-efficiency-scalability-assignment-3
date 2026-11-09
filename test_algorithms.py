import random
import unittest
from algorithms import randomized_quicksort, deterministic_quicksort
from hash_table import ChainedHashTable


class SortingTests(unittest.TestCase):
    def test_edge_cases(self):
        samples = [[], [1], [3, 3, 3], [1, 2, 3, 4], [4, 3, 2, 1],
                   [-2, 0, -2, 8, 1], list(range(300))]
        for sorter in (randomized_quicksort, deterministic_quicksort):
            for values in samples:
                with self.subTest(sorter=sorter.__name__, values=values[:5]):
                    self.assertEqual(sorter(values.copy()), sorted(values))

    def test_random_samples(self):
        rng = random.Random(77)
        for _ in range(100):
            values = [rng.randrange(-30, 31) for _ in range(rng.randrange(100))]
            self.assertEqual(randomized_quicksort(values.copy(), seed=8), sorted(values))
            self.assertEqual(deterministic_quicksort(values.copy()), sorted(values))


class HashTests(unittest.TestCase):
    def test_operations(self):
        table = ChainedHashTable(capacity=2, seed=5)
        for i in range(-100, 101):
            table.insert(i, str(i))
        self.assertEqual(len(table), 201)
        self.assertLessEqual(table.load_factor, 0.75)
        self.assertEqual(table.search(-1), '-1')
        table.insert(-1, 'updated')
        self.assertEqual(table.search(-1), 'updated')
        self.assertEqual(len(table), 201)
        for i in range(-100, 101):
            self.assertEqual(table.delete(i), 'updated' if i == -1 else str(i))
        self.assertEqual(len(table), 0)
        with self.assertRaises(KeyError):
            table.search(5)
        with self.assertRaises(KeyError):
            table.delete(5)
        with self.assertRaises(TypeError):
            table.insert('abc', 1)

    def test_collisions(self):
        table = ChainedHashTable(capacity=1, seed=3)
        for i in range(40):
            table.insert(i * table.PRIME, i)
        for i in range(40):
            self.assertEqual(table.search(i * table.PRIME), i)


if __name__ == '__main__':
    unittest.main()
