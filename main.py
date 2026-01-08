# 14. ENG KO‘P UCHRAYDIGAN ELEMENT
nums = [int(x) for x in input().split()]
res = nums[0]
mx = 0
for x in nums:
    if nums.count(x) > mx:
        mx = nums.count(x)
        res = x
print(res)
