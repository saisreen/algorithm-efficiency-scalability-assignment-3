"""In-place three-way quicksort variants, with explicit stacks."""
import random


def quicksort(values, randomized=True, seed=None):
    """Sort a mutable list in place; randomized pivots are uniform in [lo, hi]."""
    rng = random.Random(seed)
    stack = [(0, len(values) - 1)]
    while stack:
        lo, hi = stack.pop()
        while lo < hi:
            pivot_index = rng.randrange(lo, hi + 1) if randomized else lo
            pivot = values[pivot_index]
            lt, i, gt = lo, lo, hi
            while i <= gt:
                if values[i] < pivot:
                    values[lt], values[i] = values[i], values[lt]
                    lt += 1
                    i += 1
                elif values[i] > pivot:
                    values[i], values[gt] = values[gt], values[i]
                    gt -= 1
                else:
                    i += 1
            # Process the smaller side immediately; defer the larger side.
            if lt - lo < hi - gt:
                if gt + 1 < hi:
                    stack.append((gt + 1, hi))
                hi = lt - 1
            else:
                if lo < lt - 1:
                    stack.append((lo, lt - 1))
                lo = gt + 1
    return values


def randomized_quicksort(values, seed=None):
    return quicksort(values, randomized=True, seed=seed)


def deterministic_quicksort(values):
    return quicksort(values, randomized=False)
