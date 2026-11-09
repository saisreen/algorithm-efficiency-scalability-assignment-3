"""Reproducible comparisons: paired input arrays and median of repeated trials."""
import csv
import random
import statistics
import time
from pathlib import Path
from algorithms import randomized_quicksort, deterministic_quicksort

SIZES = (200, 500, 1000, 2000)
TRIALS = 7


def make_data(kind, size, seed):
    rng = random.Random(seed)
    if kind == 'random':
        return [rng.randrange(-10 * size, 10 * size) for _ in range(size)]
    if kind == 'sorted':
        return list(range(size))
    if kind == 'reverse':
        return list(range(size, 0, -1))
    if kind == 'repeated':
        return [rng.randrange(5) for _ in range(size)]
    raise ValueError(kind)


def run(output='results.csv'):
    rows = []
    for kind in ('random', 'sorted', 'reverse', 'repeated'):
        for n in SIZES:
            timings = {'randomized': [], 'first_pivot': []}
            for trial in range(TRIALS):
                data = make_data(kind, n, 2026 + trial)
                expected = sorted(data)
                for name, sorter in (('randomized', randomized_quicksort),
                                     ('first_pivot', deterministic_quicksort)):
                    sample = data.copy()
                    start = time.perf_counter_ns()
                    if name == 'randomized':
                        sorter(sample, seed=10000 + trial)
                    else:
                        sorter(sample)
                    elapsed = (time.perf_counter_ns() - start) / 1e6
                    assert sample == expected
                    timings[name].append(elapsed)
            rows.append({'distribution': kind, 'n': n,
                         'randomized_ms': round(statistics.median(timings['randomized']), 4),
                         'first_pivot_ms': round(statistics.median(timings['first_pivot']), 4)})
    with Path(output).open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    return rows


if __name__ == '__main__':
    for result in run():
        print(result)
