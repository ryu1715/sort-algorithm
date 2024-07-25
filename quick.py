from typing import List

def quick_sort(nums: List[int])-> List[int]:
    # リストが空または１つだけの場合はそのまま返す
    if len(nums) <= 1:
        return nums

    # 最初の値を基準値として使用する
    pivot = nums[0]

    # 基準値よりも小さい数を格納
    less = [i for i in nums[1:] if i <= pivot]
    # 基準値よりも小さい数を格納
    greater = [i for i in nums[1:] if i > pivot]

    # 再起的にソートして結果を結合
    return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    import random
    input_nums = [random.randint(0,1000) for i in range(10)]

    print(quick_sort(input_nums))
