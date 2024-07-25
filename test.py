import unittest
from bubble import bubble_sort
from quick import quick_sort

class TestSortAlgorithms(unittest.TestCase):

    def setUp(self):
        # 共通のテストケースを定義
        self.test_cases = [
            ([], []),  # 空のリスト
            ([1], [1]),  # 要素が1つのリスト
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # 既にソートされたリスト
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # 逆順のリスト
            ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]),  # ランダムなリスト
            ([2, 3, 2, 1, 1, 2], [1, 1, 2, 2, 2, 3])  # 重複要素を含むリスト
        ]

    def test_bubble_sort(self):
        # バブルソートに対するテストを実行
        for unsorted_list, expected_sorted_list in self.test_cases:
            with self.subTest(unsorted_list=unsorted_list):
                self.assertEqual(bubble_sort(unsorted_list.copy()), expected_sorted_list)

    def test_quick_sort(self):
        # クイックソートに対するテストを実行
        for unsorted_list, expected_sorted_list in self.test_cases:
            with self.subTest(unsorted_list=unsorted_list):
                self.assertEqual(quick_sort(unsorted_list.copy()), expected_sorted_list)

if __name__ == '__main__':
    unittest.main()
