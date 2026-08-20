# Python Linear Search

## Overview

This program searches for a given element in an array using
the linear search technique.

The array is checked element by element until the required
key is found.

## Example

Given:

[10, 20, 30, 40, 50]

Key:

30

Output:

2

## How It Works

The program starts from the beginning of the array and compares
each element with the key.

If the key is found, its index is returned.

If the key is not found, the function returns `-1`.

## Concepts Covered

- Lists
- Functions
- Loops
- Array indexing
- Linear Search
- Searching algorithms

## Complexity

### Time Complexity

- Best Case: O(1)
- Worst Case: O(n)

### Space Complexity

O(1)

## Repository Structure

Python-Linear-Search/
│
├── LinearSearch.py
└── README.md

## Note

The search loop currently starts from index `1`, so it skips
the first element of the array.
