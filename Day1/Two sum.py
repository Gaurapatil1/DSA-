# Two sum problem
def two_sum(nums, target):
    seen = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index
num = [2, 7, 11, 15]
target = 9
result = two_sum(num, target)
if result:
    print(f"Indices of the two numbers that add up to {target} are: {result}")
else:
    print("No two numbers add up to the target.")
# Example usage
# nums = [2, 7, 11, 15]
# target = 9
# result = two_sum(nums, target)
# if result:
#   print(f"Indices of the two numbers that add up to {target} are: {result}")
# else:
# print("No two numbers add up to the target.")
