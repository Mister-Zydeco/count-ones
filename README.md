---
title: Counting occurrences of 1s in digits in a range
---

Given a positive integer $n$, how many times does the digit 1
occur in the decimal expansions integers $k with $1 \le k \le n$ ?

For instance if $n = 23$, we count

**1**, 2, 3, ..., **1**0, **11**, **1**2, ..., **1**9, 20, 2**1**, 22, 23

for a total of 13 1s in the range.

We can write a python one-liner to compute this for any integer $n$ > 1:
```
def count_ones_ez(n: int) -> int:
    return sum(1 for y in range(1, n + 1) for x in str(y) if x == '1')
```

This is quite expensive computationally. We will do much better.
Nonetheless, this one-liner does have the advantage that it does exactly
what is asked -- scan the decimal expansion of the integers in range for 1s
and sum the counts -- and so after verifying that it works correctly for
a few small examples, we are very confident of its correctness. We can and
will use it for testing a more efficient algorithm.

I got this problem from Leetcode. It is classified there as a "hard"
problem, which seems a little odd to me.  We provide a description of the
algorithm including some discussion of computational complexity, a
 source file impelementing the algorithm, and a unit test file
which verifies that the one-liner and our more efficient function provide
the same answer for a couple of hundred values of $n$ less than 1,000,000.

There is a lot of stuff here to support sphinx, which I used to write
docs/source/algorithm.rst. The files of real interest to us are
count_ones.py, test/count_ones_test.py, this README, and
docs/_build/html/algorithms.html.

To run the unit tests, clone this repository, go to the test
subdirectory of the top-level directory, and run

```
$ PYTHONPATH=.. python count_ones_test.py
```
