eng =int(input("enter your score for english🏴󠁧󠁢󠁥󠁮󠁧󠁿:"))
maths =int(input("Enter your score for maths🧮: "))
sci =int(input("Enter your score for science🧪:"))

total = eng + maths + sci
avg = total / 3

if avg >= 85:
    print("grade A+🏆")
elif avg >= 75 and avg < 85:
    print("Grade A😄") 
elif avg >= 60 and avg < 75:
    print("Grade B😉")
elif avg >= 50 and avg < 60:
    print("Grade C🫤")
elif avg >= 40 and avg < 50:
    print("Grade D😕")
else:
    print("Oh no! You failed!😢")