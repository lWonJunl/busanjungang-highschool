money=int(input("Total Money:"))

m50=money//50000
money=money%50000

m10=money//10000
money=money%10000

m5=money//5000
money=money%5000

m1=money//1000
money=money%1000

print("50000원: %d장\n10000원: %d장\n5000원: %d장\n10000원: %d장" % (m50,m10,m5,m1))
