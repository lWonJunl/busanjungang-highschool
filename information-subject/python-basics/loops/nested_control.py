print("[내신 등급 계산 프로그램]")

myGrade=0
sumGrade=0
termCount=int(input("계산할 학기 수 입력(1~6):"))

for i in range(termCount):
  totUnit=0
  totGrade=0
  print(i+1,end="")
  subjectCount=int(input("학기 과목수 입력:"))
  for j in range(subjectCount):
    print(j+1,end="")
    unit=int(input("과목 단위 수:"))
    grade=int(input("석차 등급:"))
    totUnit+=unit
    totGrade+=grade*unit
  termGrade=totGrade/totUnit
  sumGrade+=termGrade
myGrade=sumGrade/termCount

option=int(input("수준 출력 여부(1.출력, 2.미출력):"))

print("전체 내신 등급은",myGrade,"입니다")
if option==1:
  if myGrade<=3:
    myLevel="상위권"
  elif myGrade<=6:
    myLevel="중위권"
  else:
    myLevel="하위권"
  print("수준은",myLevel,"입니다.")
