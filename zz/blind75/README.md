# Blind 75 — LeetCode Practice Files

One folder per category, one `.py` file per problem, distilled from the
`algorithms/blind-75-leetcode.md` notes. File numbers follow the canonical
Blind 75 ordering (01–75), so `09-tree/68_validate_binary_search_tree.py` is
problem #68 of the list.

Every file is a runnable standalone script: the solution, then a couple of
sample calls printed at the bottom. Node classes and tiny helpers are repeated
per file rather than shared, so any file runs on its own.

```sh
cd 01-array
python 01_two_sum.py

# or the whole set
find . -name '*.py' -exec python {} \;
```

## Folder layout

| Folder | Problems | Themes |
|---|---|---|
| `01-array/` | 1–10 | hash maps, running extremes, two pointers, rotated binary search |
| `02-binary/` | 11–15 | bit tricks, 32-bit masking, fixed-width iteration |
| `03-dynamic-programming/` | 16–26 | rolling state, tabulation, one greedy |
| `04-graph/` | 27–34 | grid BFS/DFS, topological sort, union-find |
| `05-interval/` | 35–39 | sort then sweep, greedy by end time, heap of end times |
| `06-linked-list/` | 40–45 | pointer rewiring, dummy heads, fast/slow runners |
| `07-matrix/` | 46–49 | in-place marking, boundary shrinking, grid DFS |
| `08-string/` | 50–59 | sliding windows, counters, palindromic centers, framing |
| `09-tree/` | 60–73 | recursion on subtrees, BST invariants, tries |
| `10-heap/` | 74–75 | bucket sort by frequency, two-heap median |

Each file names its problem and complexity in the first three lines, so
`grep -rn '^# ' .` gives a one-screen table of contents.
