print("내신 등급 계산 프로그램")
myGrade=0
totUnit=0
totGrade=0
subjectCount=int(input("과목수를 입력해 주세요: "))
for i in range(subjectCount):
    print(i+1,end=" ")
    unit=int(input("과목 단위 수: "))
    if unit==0:
      print("오류가 발생했습니다. 입력값을 확인해 주세요.")
      break
    grade=int(input("석차등급: "))
    if grade==0:
      print("오류가 발생했습니다. 입력값을 확인해 주세요.")
      break
    totUnit+=unit 
    totGrade+=grade*unit
if unit==0:
  print()
else :  
  myGrade=round(totGrade/totUnit,2)
  printLevel=input("수준을 출력하시겠습니까?(T/F): ")
  if printLevel=="T":
    if myGrade<=3:
      myLevel="상위권"
    elif myGrade<=6:
      myLevel="중위권"
    else:
      myLevel="하위권"
    print("내신 등급은",myGrade,"이고",myLevel,"입니다.")
  else :
    print("내신 등급은",myGrade,"입니다.")


                
