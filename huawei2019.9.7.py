# nums = list(map(int, input().strip().split()))

# nums = [2, 3, 1, 1, 4]

# length = len(nums)

# start = length // 2

# dp = [0 for _ in range(len(nums))]

# while length >0 : 
# 	for i in range(start):
# 		if length == nums[i] + i:



# 立方体切割问题
while 0:
	x, y, z, k = 3, 3, 3, 3


	times_of_3 = k // 3
	k_res = k % 3

	qie = x - 1 


	if qie >= times_of_3:
		if k_res == 0:
			print(times_of_3**3 )
		elif k_res == 1:
			print(times_of_3**3 + (times_of_3**2) )
		elif k_res == 2:
			print(times_of_3**3 + (times_of_3**2) + times_of_3**2 + 1)  ### 还要补上

	else:
		print(qie**3)



'''
最大公约数
'''
class Solution:
    def canMeasureWater(self, x, y, z ):
        global hcf
        if x + y < z:
            return False
        smaller = min(x, y)
        for i in range(1, smaller+1):
            if x % i == 0 and y % i == 0:
                hcf = i  # 存在更大的值时会覆盖原来的hcf，最后剩下最大公约数
        if z % hcf == 0:
            return True
        return False

s = Solution()
print(s.canMeasureWater(3, 8, 2))




