def data_input():
    a = open('numbers.txt')
    nums = [int(num.strip()) for num in a]
    return nums


def func(nums):
    nums.sort()
    mid = nums[len(nums) // 2]
    count = 0
    for i in nums:
        count += abs(mid - i)

    return count


def main():
    number = data_input()
    print(func(number))


if __name__ == '__main__':
    main()
