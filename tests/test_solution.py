from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        res = solution()

        self.assertEqual(['b', 'd', 'f'], res.index.tolist())
        self.assertEqual(res['name']['b'], 'Dima')
        self.assertEqual(res['name']['d'], 'James')
        self.assertEqual(res['name']['f'], 'Michael')

