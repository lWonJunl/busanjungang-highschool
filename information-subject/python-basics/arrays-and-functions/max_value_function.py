def greatest(data):
  greater=data[0]
  for i in range(1,len(data)):
    if greater<data[i]:
      greater=data[i]
  return greater

nums=[87,65,41,23,54,18,94,54,11,85,94,12,36]

print(greatest(nums))
