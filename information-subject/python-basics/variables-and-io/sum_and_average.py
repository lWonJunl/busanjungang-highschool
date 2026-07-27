nums=[int(k) for k in input().split()]
cnt=len(nums)
total=sum(nums)
avg=round(total/cnt,2)
print("합계=",total)
print("평균=",avg)
