Sci=float(input("enter science marks"))
math=float(input("enter math marks"))
ssc=float(input("enter ssc marks"))
total=Sci+math+ssc
print("total marks is ",total)
average=total/300*100
print("your percentage is ", average)
if average >= 90 and average<=100:
    print("you got A1 grade")
elif average>=80 and average<90:
    print("you got A2 grade")
elif average>=70 and average<80:
    print("you got B1 grade")
elif average>=60 and average<70:
    print("you got B2 grade")
elif average>=50 and average<60:
    print("you got C grade")
elif average<50:
    print("you failed")
else:
    print("enter marks under 100")