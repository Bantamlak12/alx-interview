#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


nums = [0] * 10000
for i in range(10000):
    nums[i] = i


print("Winner: {}".format(isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2]))) # Maria
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3]))) # Ben
print("Winner: {}".format(isWinner(5, [1, 2, 3, 4, 5]))) # Ben
print("Winner: {}".format(isWinner(4, [11, 30, 1, 7]))) # Ben
print("Winner: {}".format(isWinner(6, [1, 1, 0, 0, 1, 8]))) # Ben
print("Winner: {}".format(isWinner(1, [1]))) # Ben
print("Winner: {}".format(isWinner(0, [0]))) # None
print("Winner: {}".format(isWinner(-1, [10]))) # None
print("Winner: {}".format(isWinner(10000, nums))) # 10000
