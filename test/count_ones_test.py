import unittest
from count_ones import count_ones
from random import randrange

def count_ones_ez(n: int) -> int:
   return sum(1 for y in range(1, n + 1) for x in str(y) if x == '1')


class TestCountOnes(unittest.TestCase):
    def test_23(self):
        ez_count, count = count_ones_ez(23), count_ones(23)
        self.assertEqual(ez_count, count)

    def test_a_bunch(self):
        n_tests, max_n = 200, 1_000_000
        seed = 1234567
        ns = []
        for _ in range(n_tests):
            n = randrange(1, max_n)
            ns.append(n)
            ez_count, count = count_ones_ez(n), count_ones(n)
            self.assertEqual(ez_count, count)
            if (_ + 1) % 50 == 0:
                print(f'Completed {_+1} cases...')
            
        print(f"n's tested: {ns}")
if __name__ == '__main__':
    unittest.main()
