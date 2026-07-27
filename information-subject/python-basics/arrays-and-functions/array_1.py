# 태양계의 8개 행성의 크기를 1차원 배열인 planetScale에 순서대로 저장한다.
planetScale = [2440, 6052, 6378, 3390, 69911, 58232, 25362, 24622]

maxScale=planetScale[0]

for i in range(1,8):
  if maxScale<planetScale[i]:
    maxScale=planetScale[i]
print(maxScale)
