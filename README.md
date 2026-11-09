# Assignment 3 — Algorithm Efficiency and Scalability

This repository contains an original Python study of randomized Quicksort, deterministic first-pivot Quicksort, and a dynamically resized hash table with separate chaining.

## Files
- `algorithms.py` — both Quicksort variants with three-way partitioning.
- `hash_table.py` — integer-key chaining hash table with insert/search/delete and resizing.
- `test_algorithms.py` — automated correctness and edge-case tests.
- `benchmark.py` — reproducible performance experiment.
- `results.csv` — measured median execution times from the included run.
- `Assignment_3_Report.docx` — theory, empirical results, interpretation, and references.

## Requirements
Python 3.9 or newer. No third-party libraries are needed.

## Run
```bash
python -m unittest -v
python benchmark.py
```
The benchmark rewrites `results.csv` with measurements from your machine. Times will differ by machine and Python version.

## Summary
Randomized Quicksort has expected O(n log n) time for distinct keys; first-pivot Quicksort can degrade on unfavorable input. Three-way partitioning efficiently handles repeated keys. Chaining supports expected O(1 + load_factor) search, insert-with-update-check, and delete under simple uniform hashing. The hash table grows above 0.75 load and shrinks below 0.20 load. The universal hash construction applies to distinct residues modulo 2^61 - 1; keys congruent modulo this prime can still collide.

## Submission
Create a GitHub repository, upload all files from this folder (not the ZIP itself), and submit the repository URL. Replace the student/course placeholders in the report first.
