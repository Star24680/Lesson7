Eng=int(input("ENTER ENG MARKS"))
Sci=int(input("ENTER SCIENCE MARKS"))
Math=int(input("ENTER MATH MARKS"))
Geo=int(input("ENTER GEOGRAPHY MARKS"))
His=int(input("ENTER HISTORY MARKS"))
Total=Eng+Sci+Math+Geo+His
TOTAL=Total/5
if TOTAL>=90:
   print("A+")
elif TOTAL>70 and TOTAL<=89:
    print("B")
else:
    print("Fail")
