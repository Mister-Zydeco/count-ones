.. meta::
     :title: Count ones algorithm

We repeat the straightforward one-liner that computes the number of times
1 occurs as a digit in all integers :math:`k` with :math:`1 \le k \le n`
for some given positive integer :math:`n`:

.. code-block::

    def count_ones_ez(n: int) -> int:
        return sum(1 for y in range(1, n + 1)
                   for x in str(y) if x == '1')

This computation is a loop in whose :math:`k`-th pass we do :math:`O(1)`
work the :math:`k`-th digit of :math:`n`. The number of digits in :math:`k` is
:math:`O(log(k))`. Further, we observe that if :math:`n` is large, over
90% of the integers have at least :math:`d-1` digits, where :math:`d` is
the number of digits in :math:`n`. From these facts, it can be seen that
the time complexity of our one-liner is :math:`O(n\,log(n))`. It is likely to
take us a very long time to compute this if :math:`n` has 100 digits.


We can do much better by counting how many :math:`1`s occur in each of the
:math:`d` digit positions among integers :math:`k` with :math:`1 \le n`.
Let’s discuss this for :math:`n = 415083`. How many times does 1 appear
in the 1000s digit among all numbers in :math:`U`? These appearances
fall in blocks of numbers whose last four digits are in the range
:math:`S = {1000, 10001, ..., 1999}`. Each block has 1000 elements, and
there are 42 such blocks
:math:`\{10000c + x: c = 0, 1, .. 41 \text{ and }x \in S\}`. Thus, 1
occurs in the 1000s digit of positive numbers :math:`\le 415083` a
total of 42000 times.

To generalize, when the :math:`10^k`\ s digit of :math:`n` is greater
than 1, the positive numbers :math:`\le n` where that digit equals 1 are
found in complete blocks where the k+1 least significant digits can form
any of the :math:`10^k` numbers between :math:`10^k` and
:math:`2 \cdot 10^k - 1`; and there will be :math:`n//10^{k+1} + 1`
choices for the higher-order digits (including the empty sequence of
higher-order digits) occurring to the left of the 1 in digit :math:`k`.
We are using python’s // notation for integer divison (e.g, 7 // 2 = 3).

Now let’s consider how many times 1 occurs in the 100s digit of numbers
in :math:`U`. In :math:`n` itself, the 100s digit is 0. This time we
have complete blocks 100-199, **1**\ 100-\ **1**\ 199,
**2**\ 100-\ **2**\ 199,…, **414**\ 100-\ **414**\ 199. This time there
are only :math:`n//10^k = 415` blocks: the choices for the higher-digits
(the empty choice plus any number from 1 to 414). The difference with
the above is that we have too few numbers above 415000 to make a
contribution to the 1s count in the 100s digit. And so we find that 1
occurs in the 100s digit 41500 times.

Finally, what if :math:`n` has one of its digits equal to 1? In our
present example 415083, the 10000s digit of :math:`n` is 1. How many
times does 1 occur in the 10000s digit of numbers in :math:`U`? This
time there are 4 complete blocks
:math:`{100000c + x: 0 \le c \le 3, 10000 \le x \le 19999}` of 10000
numbers each, plus one partial block 41\ **0000**, 41\ **0001**, …,
41\ **5083** with 5084 numbers. More generally, if the :math:`10^k`
digit of :math:`n` is 1, there are :math:`n \% 10^{k+1} + 1` numbers in
the final partial block in :math:`U` where the :math:`10^k` digit is 1.
We are using the python notation :math:`\%` for the modulo operator
(:math:`a \% b` is the remainder when the integer :math:`a` is divided
by the integer :math:`b`).

Tying all this together in a formula, let’s denote by :math:`f(n,k)` the
total number of times 1 occurs in the :math:`k`-th digit of positive
numbers :math:`\le n`. Let’s denote the :math:`k`-th digit of :math:`n`
itself by :math:`D(k, n)`.

Then we have

.. math::

   f(n, k) = \begin{cases}
                    n//10^{k+1} + 1 \text{ if } D(n,k) \gt 1 \\
                    n//10^{k+1} \text{ if } D(n, k) = 0 \\
                    n//10^{k+1} + n \% 10^k + 1 \text{ if } D(n, k) = 1 \\
                    \end{cases}

Finally, the function we seek is the sum of these over all digit
positions:

.. math:: F(n) = \sum_{k=0}^{d} f(n, k)

By keeping powers of 10 around, we can compute :math:`f` for each digit in
:math:`O(1)` steps. There are :math:`O(log(n))` digits in :math:`n`, and
so the time complexity to compute :math:`F` is also :math:`O(log(n))`.
