from typing import List

# バブルソート
def bubble_sort(nums: List[int]) -> List[int]:
    len_nums = len(nums)

    # リストが空または１つだけの場合はそのまま返す
    if len_nums <= 1:
        return nums

    for i in range(len_nums):
        # 隣接する要素を比較して順序が逆の場合に交換
        for j in range(len_nums - 1 - i):
            if nums[j] > nums[j+1]:
                # 隣接する要素を比較し、必要なら交換
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums

if __name__ == '__main__':
    import random
    nums = [random.randint(0,1000) for i in range(10)]
    print(bubble_sort(nums))
